"""
Higgs Voice Selector - ComfyUI Custom Node
A tag selector for Higgs voice generation (emotion, style, SFX, prosody)
"""


class HiggsVoiceSelector:
    """Higgs 语音标签选择器 - 用户选择中文标签，输出完整格式标签"""

    CATEGORY = "prompt/Higgs-Voice"
    FUNCTION = "generate_higgs_tags"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("标签输出",)

    # ==================== 情感标签（Emotion）21个 ====================
    情感选项 = [
        "——",
        "兴高采烈",
        "愉悦/好笑",
        "热情",
        "坚定",
        "骄傲",
        "满足",
        "喜爱",
        "宽慰",
        "沉思",
        "困惑",
        "惊讶",
        "敬畏",
        "渴望",
        "激动",
        "愤怒",
        "恐惧",
        "厌恶",
        "痛苦",
        "悲伤",
        "羞耻",
        "无助",
    ]

    情感映射 = {
        "兴高采烈": "<|emotion:elation|>",
        "愉悦/好笑": "<|emotion:amusement|>",
        "热情": "<|emotion:enthusiasm|>",
        "坚定": "<|emotion:determination|>",
        "骄傲": "<|emotion:pride|>",
        "满足": "<|emotion:contentment|>",
        "喜爱": "<|emotion:affection|>",
        "宽慰": "<|emotion:relief|>",
        "沉思": "<|emotion:contemplation|>",
        "困惑": "<|emotion:confusion|>",
        "惊讶": "<|emotion:surprise|>",
        "敬畏": "<|emotion:awe|>",
        "渴望": "<|emotion:longing|>",
        "激动": "<|emotion:arousal|>",
        "愤怒": "<|emotion:anger|>",
        "恐惧": "<|emotion:fear|>",
        "厌恶": "<|emotion:disgust|>",
        "痛苦": "<|emotion:bitterness|>",
        "悲伤": "<|emotion:sadness|>",
        "羞耻": "<|emotion:shame|>",
        "无助": "<|emotion:helplessness|>",
    }

    # ==================== 风格标签（Style）3个 ====================
    风格选项 = [
        "——",
        "唱歌",
        "大喊",
        "低语/耳语",
    ]

    风格映射 = {
        "唱歌": "<|style:singing|>",
        "大喊": "<|style:shouting|>",
        "低语/耳语": "<|style:whispering|>",
    }

    # ==================== 音效标签（SFX）9个 ====================
    音效选项 = [
        "——",
        "咳嗽",
        "笑",
        "哭",
        "尖叫",
        "打嗝",
        "哼唱",
        "叹气",
        "抽鼻子",
        "打喷嚏",
    ]

    音效映射 = {
        "咳嗽": "<|sfx:cough|>",
        "笑": "<|sfx:laughter|>",
        "哭": "<|sfx:crying|>",
        "尖叫": "<|sfx:screaming|>",
        "打嗝": "<|sfx:burping|>",
        "哼唱": "<|sfx:humming|>",
        "叹气": "<|sfx:sigh|>",
        "抽鼻子": "<|sfx:sniff|>",
        "打喷嚏": "<|sfx:sneeze|>",
    }

    # ==================== 韵律标签（Prosody）10个 ====================
    韵律选项 = [
        "——",
        "极慢速",
        "慢速",
        "快速",
        "极快速",
        "低音调",
        "高音调",
        "短停顿",
        "长停顿",
        "表现力强",
        "表现力平缓",
    ]

    韵律映射 = {
        "极慢速": "<|prosody:speed_very_slow|>",
        "慢速": "<|prosody:speed_slow|>",
        "快速": "<|prosody:speed_fast|>",
        "极快速": "<|prosody:speed_very_fast|>",
        "低音调": "<|prosody:pitch_low|>",
        "高音调": "<|prosody:pitch_high|>",
        "短停顿": "<|prosody:pause|>",
        "长停顿": "<|prosody:long_pause|>",
        "表现力强": "<|prosody:expressive_high|>",
        "表现力平缓": "<|prosody:expressive_low|>",
    }

    @classmethod
    def VALIDATE_INPUTS(cls, **kwargs):
        """验证多选输入的有效性"""
        validations = [
            (kwargs.get("选择情感", []), cls.情感选项, "选择情感"),
            (kwargs.get("选择风格", []), cls.风格选项, "选择风格"),
            (kwargs.get("选择音效", []), cls.音效选项, "选择音效"),
            (kwargs.get("选择韵律", []), cls.韵律选项, "选择韵律"),
        ]

        for value, valid_options, name in validations:
            # 处理多选列表
            items = cls._normalize_list(value)
            for item in items:
                if item not in valid_options:
                    return f"{name} '{item}' 不在有效选项中"
        return True

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "选择情感": (cls.情感选项, {"default": ["——"], "multi_select": True}),
                "选择风格": (cls.风格选项, {"default": ["——"], "multi_select": True}),
                "选择音效": (cls.音效选项, {"default": ["——"], "multi_select": True}),
                "选择韵律": (cls.韵律选项, {"default": ["——"], "multi_select": True}),
            }
        }

    @staticmethod
    def _normalize_list(value):
        """将各种输入格式统一为 Python 列表"""
        if value is None:
            return ["——"]
        if isinstance(value, list):
            return [str(v).strip() for v in value if v is not None and str(v).strip() != ""] or ["——"]
        if isinstance(value, str):
            # 处理字符串化的列表，如 "['item1', 'item2']"
            if value.startswith("[") and value.endswith("]"):
                try:
                    import ast
                    parsed = ast.literal_eval(value)
                    if isinstance(parsed, list):
                        cleaned = [str(v).strip() for v in parsed if v is not None and str(v).strip() != ""]
                        return cleaned if cleaned else ["——"]
                except (ValueError, SyntaxError):
                    pass
            cleaned = value.strip()
            return [cleaned] if cleaned else ["——"]
        return [str(value).strip()]

    def generate_higgs_tags(self, 选择情感, 选择风格, 选择音效, 选择韵律):
        """生成 Higgs 语音标签"""
        # 统一为列表格式
        情感列表 = self._normalize_list(选择情感)
        风格列表 = self._normalize_list(选择风格)
        音效列表 = self._normalize_list(选择音效)
        韵律列表 = self._normalize_list(选择韵律)

        # 收集所有选中的标签
        result_tags = []

        for item in 情感列表:
            if item != "——":
                tag = self.情感映射.get(item, "")
                if tag:
                    result_tags.append(tag)

        for item in 风格列表:
            if item != "——":
                tag = self.风格映射.get(item, "")
                if tag:
                    result_tags.append(tag)

        for item in 音效列表:
            if item != "——":
                tag = self.音效映射.get(item, "")
                if tag:
                    result_tags.append(tag)

        for item in 韵律列表:
            if item != "——":
                tag = self.韵律映射.get(item, "")
                if tag:
                    result_tags.append(tag)

        # 用逗号拼接所有标签
        output = ", ".join(result_tags)
        return (output,)


# 节点注册
NODE_CLASS_MAPPINGS = {
    "HiggsVoiceSelector": HiggsVoiceSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HiggsVoiceSelector": "Higgs 语音标签选择器"
}
