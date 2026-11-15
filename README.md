# MGU-CN-XIAOBAI

面向已装 MGU Store 的 BMW iDrive 主机。汉化署名为抖音「小白科技杂物社」、BiliBili「小白151」、GitHub [JackieZ123430](https://github.com/JackieZ123430)。

| 项目 | 收录内容 |
| --- | --- |
| [iDrive 7 Apps](https://github.com/JackieZ123430/idrive7-apps-cn) | 15 个应用，包括故障扫描、换挡提示、暖机监测、车辆数据和加速测试 |
| [BMW Apps](https://github.com/alexp50/bmw-apps/pull/3) | 15 个应用，包括车辆健康、行程、抬头显示、胎压与底盘相关应用 |
| [Cluster Themes](https://github.com/bimmer-lab/apps/pull/13) | 仪表主题选择与设置的简体中文界面 |
| [Spotify](https://github.com/hexlay/idrive7-custom-apps/pull/3) | 简体中文界面与中文媒体标题支持 |
| [RideTube](https://github.com/JustAnotherPU/ridetube/pull/3) | 简体中文界面与设置 |
| [BMW 天气](https://github.com/flash8523/bmw-weather-mgu/pull/1) | 简体中文天气界面、设置和小组件 |
| [MGU Browser](https://github.com/pllanaio/mgu-browser/pull/12) | 简体中文界面与字体改动，应用按车机语言选择界面 |
| [MGU Store](https://github.com/robertnisipeanu/mgu-store/pull/63) | 官方发行版，已收录中文译文并跟随车机语言 |

目录中的 **微信 ppppphhjjj** 是联系条目。详情页仅显示联系方式，Store 会拒绝安装请求。

## 发布到 Gitee

将本目录中的文件提交到公开仓库的根目录，保留 `catalog.json`、`packages/` 和图标的相对位置。以 `main` 分支和 `MGU-CN-XIAOBAI` 仓库为例，在 MGU Store 的「软件源 → 添加软件源」中填入：

```text
https://gitee.com/xiaobai-151/mgu-cn-xiaobai/raw/main/catalog.json
```

发布后应先确认未登录时也能读取原始 JSON 和包文件，再到车机添加。部分组件保留 GitHub 上游下载地址，其中包含超出 Gitee 普通仓库单文件体积的 Chromium 引擎。车机安装这些项目或依赖时需能访问相应地址。

目录中 35 个汉化安装包面向 ID7。安装包内保留原项目的应用 ID，并使用 MGU Store 支持的三段式版本号。同一 ID 的官方源和汉化源并存时，Store 可能优先选择较新版本或该应用原来的安装来源。添加源后可在来源详情中确认对应条目。

`provenance.json` 记录汉化构建版本和对应 GitHub 原项目或 PR。按 MGU Store 的发行格式打包，安装时由车机生成所需的 BMW OAP SDK。各应用及组件沿用原作者的许可。

电脑版 SSH 启用工具的简体汉化在 [上游 PR #4](https://github.com/cauliflowermossgrape/idrive7-8-ssh-root/pull/4) 中，使用 Windows 桌面工具的安装方式。
