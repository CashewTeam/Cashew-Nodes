bl_info = {
    "name": "Cashew Nodes 腰果节点组",
    "version": (1, 1, 0),
    "blender": (3, 0, 0),
    "category": "Assets",
}

import bpy
import os

# 定义资产库名称，资产库目录名需要与资产库名称相同 
ASSET_LIBRARY_NAME = "Cashew Nodes"

def load_assets_library():
    # 获取当前插件的路径
    addon_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(addon_dir, ASSET_LIBRARY_NAME)
    
    # 检查资产库是否已经存在，避免重复加载
    if ASSET_LIBRARY_NAME in [lib.name for lib in bpy.context.preferences.filepaths.asset_libraries]:
        print(f"Asset library '{ASSET_LIBRARY_NAME}' is already loaded")
        return
    
    if os.path.exists(assets_dir) and os.path.isdir(assets_dir):
        # 添加资产库
        bpy.ops.preferences.asset_library_add(directory=assets_dir)
        print(f"Asset library '{ASSET_LIBRARY_NAME}' loaded from {assets_dir}")
    else:
        print(f"Assets folder not found in {assets_dir}")


def unload_assets_library():
    # 尝试移除资产库
    libraries = bpy.context.preferences.filepaths.asset_libraries
    for library in libraries:
        if library.name == ASSET_LIBRARY_NAME:
            libraries.remove(library)
            print(f"Asset library '{ASSET_LIBRARY_NAME}' removed")
            return
    print(f"No asset library named '{ASSET_LIBRARY_NAME}' found")

# 使用 bpy.app.timers 延迟执行加载资产库的操作
def load_assets_with_delay():
    load_assets_library()
    return None  # 返回 None 表示定时器不再重复调用

# 注册函数
def register():
    # 延迟加载资产库，确保上下文已准备好
    bpy.app.timers.register(load_assets_with_delay)

# 注销函数
def unregister():
    unload_assets_library()

if __name__ == "__main__":
    register()
