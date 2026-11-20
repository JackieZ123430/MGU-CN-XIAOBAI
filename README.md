# MGU-CN-XIAOBAI

BMW MGU / iDrive 应用中文软件源。汉化与维护：小白科技杂物社 · BiliBili 小白151 · GitHub JackieZ123430。

FREE APPS IF PAID PLEASE RETURN · 免费应用请勿付费。

## 添加软件源

在 MGU Store 中添加以下根目录 catalog.json：

```
https://raw.githubusercontent.com/JackieZ123430/MGU-CN-XIAOBAI/refs/heads/main/catalog.json
```

安装包通过 GitHub Releases 公开下载，车机无需登录 GitHub。既有相对路径安装包仍保留，便于回退。

## 2026-11-20 更新

本次逐项检查原目录的 69 项应用和组件，更新落后版本、补齐中文说明与新版界面文字，并增加 5 个首页组件。目录现有 74 项，61 项版本更新或新增。已是当前版本的组件保留原版本。

中文构建保留上游英文 app.json、应用标识、信号接口和设置值。中文修订的三段版本为 `major.minor.(上游 patch × 100 + 中文修订号)`，例如上游 `0.3.1` 对应中文修订 `0.3.101`。真实上游版本、对应公开源码和提交记录见 [provenance.json](provenance.json) 与包内 SOURCE.zh-CN.json。后续中文修订必须增加版本，不替换已发布版本的安装包。

| 新增首页组件 | 作用 |
| --- | --- |
| aref_carcare | 车辆养护：独立保养周期与首页组件 |
| aref_carwatch | 车辆监控：行程、故障和失火事件 |
| aref_carlyrics | 车载歌词：读取当前曲目并联网获取歌词 |
| aref_eta | 导航到达时间：Apple Maps 到达时间及首页组件 |
| gif_home | GIF 首页组件：动画、上传和显示设置 |

ETA 的仪表显示需要 cluster-render，并可能与其他仪表显示应用竞争；首页组件与仪表显示分别验证。台架上先保留现有投射设置。

汽水音乐 **0.2.5 Beta** 补齐 `mguInternet: true`，让安装器自动登记联网名单。安装依赖 mgu-uplink 只提供联网组件，应用自己的声明才触发出网登记。系统日期、Wi-Fi 路由和账号音频权限仍分别影响网络和播放结果。此版保持 0.2.4 的界面、播放代码和应用数据结构。

本机构建、语言隔离、字体字形、依赖闭合和安装包校验已经通过。实机安装、HMI 画面、车辆信号及实际声音属于不同验证项，当前状态以 [VALIDATION-20261120.md](VALIDATION-20261120.md) 为准。

## 源码与上游汉化 PR

保留原项目许可证与作者声明。中文署名只显示于中文构建。公开通用 Kit 安装包不包含提取的 BMW oap-sdk，由车机部署流程提供本机 SDK。

- [arefahmad/idrive7-apps](https://github.com/arefahmad/idrive7-apps/pull/2)：当前中文修订已提交，是否合并以上游状态为准。
- [NamelsMissing/mgu-apps](https://github.com/NamelsMissing/mgu-apps/pull/9)：当前中文修订已提交，是否合并以上游状态为准。
- [cauliflowermossgrape/idrive7-apps](https://github.com/cauliflowermossgrape/idrive7-apps/pull/217)：当前中文修订已提交，是否合并以上游状态为准。
- [bimmer-lab/apps](https://github.com/bimmer-lab/apps/pull/30)：当前中文修订已提交，是否合并以上游状态为准。
- [hexlay/idrive7-custom-apps](https://github.com/hexlay/idrive7-custom-apps/pull/4)：当前中文修订已提交，是否合并以上游状态为准。
- [JustAnotherPU/ridetube](https://github.com/JustAnotherPU/ridetube/pull/16)：当前中文修订已提交，是否合并以上游状态为准。
- [giuseppesalatino-boop/mgu-apps](https://github.com/giuseppesalatino-boop/mgu-apps/pull/2)：当前中文修订已提交，是否合并以上游状态为准。
- [alexp50/bmw-apps](https://github.com/alexp50/bmw-apps/pull/4)：当前中文修订已提交，是否合并以上游状态为准。
- [pllanaio/mgu-browser](https://github.com/pllanaio/mgu-browser/pull/13)：当前中文修订已提交，是否合并以上游状态为准。

各中文源码仓库也提供根目录 catalog.json；安装包引用本仓库的 GitHub Release，避免在多个来源重复维护不同字节的同版本包。联系条目只展示信息，不能下载安装。

## 首页组件中文显示修订 2

本轮进一步修复了 8 款带组件应用的中文传输与资源打包。缩小组件通过自己的 UTF-8 字符串资源显示中文；大组件固定标签翻译为中文，歌曲、歌手和歌词按原文显示。新增 [Aref #3](https://github.com/arefahmad/idrive7-apps/pull/3) 跟进显示修复；此前 Aref #2 已被上游合并。
