"""Version the verified music package with its deployment internet declaration.

The Wi-Fi connection is managed by mgu-uplink. mguInternet is the deployer's
per-application enrollment flag; an updater dependency alone does not enroll it.
No networking daemon, credentials, player implementation or HMI layout is added.
"""
import argparse,gzip,hashlib,io,json,pathlib,tarfile

BASE_QISHUI_SHA256='bb5652e129d8e38f72ce50f763add5df12aae1d26699c50a5491b94ecd804eb2'

def build(source,output,provider,old_version,version):
    if provider=='qishui':
        assert hashlib.sha256(source.read_bytes()).hexdigest()==BASE_QISHUI_SHA256,'Unexpected public base package'
    files={};changed=[]
    with tarfile.open(source) as archive:
        for member in archive:
            assert member.isfile() and not member.name.startswith('/') and '..' not in pathlib.PurePosixPath(member.name).parts
            data=archive.extractfile(member).read();original=data
            if member.name=='package.json':
                doc=json.loads(data)
                assert (doc['name'],doc['version'])==('jackie_'+provider+'_music',old_version)
                doc['version']=version;doc['mguInternet']=True
                data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
            elif member.name=='rhmiData/application.json':
                doc=json.loads(data);assert doc['application']['version']==old_version
                doc['application']['version']=version
                data=(json.dumps(doc,ensure_ascii=False,indent=2)+'\n').encode()
            if data!=original:changed.append(member.name)
            files[member.name]=(data,member.mode)
    assert sorted(changed)==['package.json','rhmiData/application.json']
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('wb') as raw,gzip.GzipFile(fileobj=raw,filename='',mode='wb',mtime=0) as gz,tarfile.open(fileobj=gz,mode='w') as archive:
        for name,(data,mode) in sorted(files.items()):
            member=tarfile.TarInfo(name);member.size=len(data);member.mode=mode
            archive.addfile(member,io.BytesIO(data))
    with tarfile.open(output) as archive:
        assert json.load(archive.extractfile('package.json'))['mguInternet'] is True
        assert not any('auth.json' in n or 'cookie.json' in n for n in archive.getnames())
    return {'id':'jackie_'+provider+'_music','version':version,'previousVersion':old_version,'changedFiles':changed,'mguInternet':True,'artifact':{'name':output.name,'size':output.stat().st_size,'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=pathlib.Path);parser.add_argument('output',type=pathlib.Path)
    parser.add_argument('--provider',choices=('qishui','netease'),default='qishui')
    parser.add_argument('--previous',default='0.2.4');parser.add_argument('--version',default='0.2.5')
    args=parser.parse_args();print(json.dumps(build(args.source,args.output,args.provider,args.previous,args.version),ensure_ascii=True))
