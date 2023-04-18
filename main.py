import re

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction 
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
import unicodeit


def tex_to_unicode(data):
    data = data[4:]
    return unicodeit.replace(data)


class TexToUnicodeExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        data = event.get_query()
        result = tex_to_unicode(data)

        if result:
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name=result,
                                             description='Enter to copy to clipboard',
                                             on_enter=CopyToClipboardAction(result)))

        else:
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name="No result",
                                             description="Type some TeX math",
                                             on_enter=DoNothingAction()))

        return RenderResultListAction(items)


if __name__ == '__main__':
    TexToUnicodeExtension().run()
