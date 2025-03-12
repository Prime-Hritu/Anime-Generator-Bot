from enum import Enum

class PicType(Enum):
    SFW = "sfw"
    NSFW = "nsfw"

class PicCategory(Enum):
    """
    It can be used as `if PicType.TYPE.value in PicCategory.CATEGORY.allowed_types`
    """
    WAIFU = "waifu"
    NEKO = "neko"
    SHINOBU = "shinobu"
    MEGUMIN = "megumin"
    BULLY = "bully"
    CUDDLE = "cuddle"
    TRAP = "trap"
    BLOWJOB = "blowjob"

    @property
    def allowed_types(self):
        allowed = {
            PicCategory.WAIFU: {"sfw", "nsfw"},
            PicCategory.NEKO: {"sfw", "nsfw"},
            PicCategory.SHINOBU: {"sfw"},
            PicCategory.MEGUMIN: {"sfw"},
            PicCategory.BULLY: {"sfw"},
            PicCategory.CUDDLE: {"sfw"},
            PicCategory.TRAP: {"nsfw"},
            PicCategory.BLOWJOB: {"nsfw"},
        }
        return allowed[self]