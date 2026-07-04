"""
Higgs Voice Selector - ComfyUI Custom Node
A tag selector for Higgs voice generation (emotion, style, SFX, prosody)
"""


class HiggsVoiceSelector:
    """Higgs 语音标签选择器 - 四个下拉框，用户选择中文标签，输出完整格式标签"""

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
    def INPUT_TYPES(cls):
        return {
            "required": {
                "情感标签": (cls.情感选项, {"default": "——"}),
                "风格标签": (cls.风格选项, {"default": "——"}),
                "音效标签": (cls.音效选项, {"default": "——"}),
                "韵律标签": (cls.韵律选项, {"default": "——"}),
            }
        }

    def generate_higgs_tags(self, 情感标签, 风格标签, 音效标签, 韵律标签):
        """生成 Higgs 语音标签"""
        result_tags = []

        if 情感标签 and 情感标签 != "——":
            tag = self.情感映射.get(情感标签, "")
            if tag:
                result_tags.append(tag)

        if 风格标签 and 风格标签 != "——":
            tag = self.风格映射.get(风格标签, "")
            if tag:
                result_tags.append(tag)

        if 音效标签 and 音效标签 != "——":
            tag = self.音效映射.get(音效标签, "")
            if tag:
                result_tags.append(tag)

        if 韵律标签 and 韵律标签 != "——":
            tag = self.韵律映射.get(韵律标签, "")
            if tag:
                result_tags.append(tag)

        output = ", ".join(result_tags)
        return (output,)


# 节点注册
NODE_CLASS_MAPPINGS = {
    "HiggsVoiceSelector": HiggsVoiceSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "HiggsVoiceSelector": "Higgs 语音标签选择器"
}
