# Cashew-Nodes（原B4D）

Cashew Nodes（原B4D）是一个由Con11制作的一个Blender节点组资产库，旨在补充和拓展Blender的功能，简化几何节点的操作，提高用户使用Blender制作动态图形和卡通渲染的效率。  
使用 [Blender-Assets-to-Add-on](https://github.com/CashewTeam/Blender-Assets-to-Add-on) 构建。  

本资产库中带由ETK字样的节点组来自Erindale制作的Erindale Toolkit：  
https://www.blendermarket.com/products/erintools  

## 当前版本
V1.2 — 适用于六分仪 Blender NPR 分支 [Porting Goo Engine and NPR prototype to Blender 5.1](https://github.com/bb-yi/blender)

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
