"""
ComfyUI Higgs Voice Selector - Custom Node
A tag selector for Higgs voice generation
"""

from .higgs_voice_select import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# 导出节点映射，供ComfyUI使用
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
