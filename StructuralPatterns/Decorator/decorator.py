# ÖRNEK 1
from abc import ABC, abstractmethod

# Component
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

# ConcreteComponent
class EmailNotifier(Notifier):
    def send(self, message):
        return f"Sending email with message: {message}"

# Decorator
class NotifierDecorator(Notifier):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def send(self, message):
        return self._wrapped.send(message)

# ConcreteDecorator
class SMSNotifierDecorator(NotifierDecorator):
    def send(self, message):
        original_message = self._wrapped.send(message)
        return f"{original_message} | Sending SMS with message: {message}"

class SlackNotifierDecorator(NotifierDecorator):
    def send(self, message):
        original_message = self._wrapped.send(message)
        return f"{original_message} | Sending Slack message with: {message}"

# Kullanım
notifier = EmailNotifier()
sms_notifier = SMSNotifierDecorator(notifier)
slack_sms_notifier = SlackNotifierDecorator(sms_notifier)

print(slack_sms_notifier.send("Hello World!"))

print("#"*70)

# ÖRNEK 2
class Text:
    def __init__(self, content):
        self._content = content

    def render(self):
        return self._content

class TextDecorator(Text):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return self._wrapped.render()

class BoldDecorator(TextDecorator):
    def render(self):
        return f"<b>{super().render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self):
        return f"<i>{super().render()}</i>"

class UnderlineDecorator(TextDecorator):
    def render(self):
        return f"<u>{super().render()}</u>"

if __name__ == "__main__":
    simple_text = Text("Hello, World!")
    print("Simple Text:", simple_text.render())

    bold_text = BoldDecorator(simple_text)
    print("Bold Text:", bold_text.render())

    italic_bold_text = ItalicDecorator(bold_text)
    print("Italic Bold Text:", italic_bold_text.render())

    fully_formatted_text = UnderlineDecorator(italic_bold_text)
    print("Fully Formatted Text:", fully_formatted_text.render())
