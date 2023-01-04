# -*- coding: utf-8 -*-

"""
jishaku.paginators (non-shim dependencies)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Paginator-related tools and interfaces for Jishaku.

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

import typing

import discord

# emoji settings, this sets what emoji are used for PaginatorInterface

_Emoji = typing.Union[str, discord.PartialEmoji, discord.Emoji]


class EmojiSettings(typing.NamedTuple):
    """
    Emoji settings, this sets what emoji are used for PaginatorInterface
    """

    start: _Emoji
    back: _Emoji
    forward: _Emoji
    end: _Emoji
    close: _Emoji


EMOJI_DEFAULT = EmojiSettings(
    start="<:previous_last:1060080704874098688>",
    back="<:previous:1060079286859599933>",
    forward=<:next:1060079422503387246>",
    end="<:next_last:1060080694707105802>}",
    close="<:stop:1060083234215559222>",
)
