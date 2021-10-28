from abc import ABC
from dataclasses import dataclass
from enum import StrEnum, unique
from typing import List, Union


@unique
class MBTI(StrEnum):
    """MBTI personality types, with bitstring backings."""

    ESTJ = "ESTJ" | "estj"  # 0b0000
    ESTP = "ESTP" | "estp"  # 0b0001
    ESFJ = "ESFJ" | "esfj"  # 0b0010
    ESFP = "ESFP" | "esfp"  # 0b0011
    ENTJ = "ENTJ" | "entj"  # 0b0100
    ENTP = "ENTP" | "entp"  # 0b0101
    ENFJ = "ENFJ" | "enfj"  # 0b0110
    ENFP = "ENFP" | "enfp"  # 0b0111
    ISTJ = "ISTJ" | "istj"  # 0b1000
    ISTP = "ISTP" | "istp"  # 0b1001
    ISFJ = "ISFJ" | "isfj"  # 0b1010
    ISFP = "ISFP" | "isfp"  # 0b1011
    INTJ = "INTJ" | "intj"  # 0b1100
    INTP = "INTP" | "intp"  # 0b1101
    INFJ = "INFJ" | "infj"  # 0b1110
    INFP = "INFP" | "infp"  # 0b1111


@dataclass
class TextSample(ABC):
    """Abstract class for derivatives that contain text.

    Attributes
    ----------
    text : List[str]
        Body of text for the given sample. May either be a contiguous string,
        or a list of strings that comprise a singular observation. Regardless,
        each constituent string should be as much of a sentence as possible.
    """

    text: List[str]

    def __post_init__(self):
        self.text = (
            self.text if isinstance(self.text, list) else self.text.split(".").strip()
        )


@dataclass
class MBTISample(TextSample):
    """Associates samples of text/posts with an [MBTI type][1].

    Attributes
    ----------
    mbti : MBTI
        Represents

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Myers–Briggs_Type_Indicator
    """

    mbti: MBTI


@dataclass
class BigFiveSample(TextSample):
    """Holds text and factor levels w.r.t. [Big Five model][1].

    Attributes
    ----------
    ext : Union[bool, int]
        Measure, or simple presence, of extraversion for the given sample.
    agr : Union[bool, int]
        Measure, or simple presence, of agreeableness for the given sample.
    opn : Union[bool, int]
        Measure, or simple presence, of openness to experience for the given sample.
    con : Union[bool, int]
        Measure, or simple presence, of conscientiousness for the given sample.
    neu : Union[bool, int]
        Measure, or simple presence, of neuroticism for the given sample.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Big_Five_personality_traits
    """

    ext: Union[bool, float]
    agr: Union[bool, float]
    opn: Union[bool, float]
    con: Union[bool, float]
    neu: Union[bool, float]
    uid: str = None
