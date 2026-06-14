import datetime
from typing import Any, Optional, Union
from discord import Colour
from discord.embeds import Embed
from discord.types.embed import EmbedType


COLOR = 0x0099ff

class ReplyEmbed(Embed):
    '''
    will improve on this later,
    but so far we can have an easily changable default color now without needing to specify it everytime
    TODO: replace all reply embeds in commands with this one,
    TODO: add more default options
    '''
    
    def __init__(
        self,
        *,
        colour: Optional[Union[int, Colour]] = COLOR,
        color: Optional[Union[int, Colour]] = COLOR,
        title: Optional[Any] = None,
        type: EmbedType = 'rich',
        url: Optional[Any] = None,
        description: Optional[Any] = None,
        timestamp: Optional[datetime.datetime] = None,
        ):
        super().__init__(colour=colour, color=color, title=title, type=type, url=url, description=description, timestamp=timestamp)
        

    def set_color(self, color) -> "ReplyEmbed":
        self.color = color
        self.colour = color
        return self

    def set_description(self, description) -> "ReplyEmbed":
        self.description = description
        return self
