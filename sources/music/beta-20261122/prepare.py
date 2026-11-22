import gzip,hashlib,io,json,pathlib,tarfile
B=pathlib.Path(__file__).resolve().parent
W=B.parent
ROOT=W.parent
SPECS=[
 ('jackie_netease_music','0.5.4','0.5.5','网易云音乐 Beta',ROOT/'outputs/jackie_netease_music@0.5.4.tgz','Entertainment_Netease_Icon.png',True),
 ('jackie_qishui_music','0.2.5','0.2.6','汽水音乐 Beta',W/'source-refresh-20261120/packages/jackie_qishui_music@0.2.5.tgz','Entertainment_Qishui_Icon.png',True),
 ('jackie_qq_community','0.1.0','0.1.1','QQ 音乐社区版 Beta',ROOT/'outputs/jackie_qq_community@0.1.0.tgz','Entertainment_QQ_Community_Icon.png',False),
 ('jackie_kugou_music','0.1.0','0.1.1','酷狗音乐 Beta',ROOT/'outputs/jackie_kugou_music@0.1.0.tgz','Entertainment_KuGou_Icon.png',False),
]
rows=[]
for app,old,new,title,src,icon,embedded in SPECS:
 files={};changed=[]
 with tarfile.open(src) as a:
  for m in a:
   assert m.isfile() and not m.name.startswith('/') and '..' not in pathlib.PurePosixPath(m.name).parts
   data=a.extractfile(m).read();original=data
   assert not m.name.startswith('node_modules/oap-sdk/')
   assert pathlib.PurePosixPath(m.name).name not in ['car-account.json','device.json','netease_config.json','qishui_config.json','kugou_config.json','qqcommunity_config.json']
   if m.name=='package.json':
    doc=json.loads(data);assert doc['name']==app and doc['version']==old
    doc.update(version=new,title=title,description=title,mguInternet=True)
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
   elif m.name=='rhmiData/application.json':
    doc=json.loads(data);assert doc['application']['version']==old
    doc['application']['version']=new;data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
   elif m.name=='npm-shrinkwrap.json':
    doc=json.loads(data)
    if doc.get('version')==old:doc['version']=new;data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
   elif m.name.startswith('rhmiData/') and '/texts/' in m.name and m.name.endswith('.json'):
    doc=json.loads(data)
    for key in ['SID_CM_QQ_ENTRY','SID_RHMI_ENT_SELECTION_QQ']:
     if key in doc:doc[key]=title
    data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
   if original!=data:changed.append(m.name)
   files[m.name]=(data,m.mode)
 out=B/(app+'@'+new+'.tgz')
 with out.open('wb') as raw,gzip.GzipFile(fileobj=raw,mode='wb',mtime=0,filename='') as gz,tarfile.open(fileobj=gz,mode='w') as a:
  for name,(data,mode) in sorted(files.items()):
   m=tarfile.TarInfo(name);m.size=len(data);m.mode=mode;a.addfile(m,io.BytesIO(data))
 candidates=[n for n in files if n.endswith('/'+icon)]
 if not candidates and app=='jackie_qishui_music':candidates=[n for n in files if n.endswith('.png') and 'Qishui' in n]
 assert candidates,(app,'missing icon')
 iconout=B/(app+'.png');iconout.write_bytes(files[candidates[0]][0])
 row={'id':app,'oldVersion':old,'version':new,'title':title,'embeddedBackend':embedded,'source':str(src),'sourceSha256':hashlib.sha256(src.read_bytes()).hexdigest(),'artifact':{'name':out.name,'size':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},'icon':iconout.name,'iconSha256':hashlib.sha256(iconout.read_bytes()).hexdigest(),'changedFiles':changed}
 rows.append(row)
(B/'prepared.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps([{'id':r['id'],'version':r['version'],'bytes':r['artifact']['size'],'changedFiles':len(r['changedFiles'])} for r in rows]))
