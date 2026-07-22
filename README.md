# Cashew-Nodes（原B4D）

Cashew Nodes（原B4D）是一个由Con11制作的一个Blender节点组资产库，旨在补充和拓展Blender的功能，简化几何节点的操作，提高用户使用Blender制作动态图形和卡通渲染的效率。  

节点文档：[docs.cashewteam.top](https://docs.cashewteam.top/docs/Cashew%20Nodes/)

## 当前版本
V1.3 — 适用于六分仪 Blender NPR 分支

 [Porting Goo Engine and NPR prototype to Blender 5.1](https://github.com/bb-yi/blender)

## 远程仓库

GitHub Pages 地址：<https://cashewteam.github.io/Cashew_Nodes/>

### Blender 扩展仓库（4.2+）

在 Blender 中打开 `编辑 > 偏好设置 > 获取扩展 > 仓库`，添加以下远程仓库地址：

<https://cashewteam.github.io/Cashew_Nodes/extensions/index.json>

该仓库包含 `Addon_releases` 中除 3.6 archive 外的所有扩展包，包括 Cashew Nodes 和 VMC Link。

### 远程资产库（5.2+）

在 `编辑 > 偏好设置 > 资产库` 中选择添加远程资产库，填入：

<https://cashewteam.github.io/Cashew_Nodes/assets/>

然后在资产浏览器中选择 `Cashew Nodes Library`，即可按需浏览和下载 `Cashew_Nodes_Library` 中的资产。

## 文件结构
```
Cashew-Nodes/
├── __init__.py                     # 插件入口，自动注册资产库
├── blender_manifest.toml           # Blender 扩展清单
├── CHANGELOG.md                    # 更新日志
├── LICENSE
├── README.md
└── Cashew_Nodes_Library/           # 资产库目录
    ├── blender_assets.cats.txt     # 资产目录定义
    ├── Cashew_Nodes.blend          # 几何节点与修改器
    └── NPR.blend                   # 三渲二着色器与合成器
```

## 已知问题
1. 破碎FX的样条模式还未制作

## 相关项目
- 构建工具：[Blender-Assets-to-Add-on](https://github.com/CashewTeam/Blender-Assets-to-Add-on)
- 六分仪 Blender NPR 分支 [Porting Goo Engine and NPR prototype to Blender 5.1](https://github.com/bb-yi/blender)
- 本库中 ETK 节点组来自 [Erindale Toolkit](https://www.blendermarket.com/products/erintools)
