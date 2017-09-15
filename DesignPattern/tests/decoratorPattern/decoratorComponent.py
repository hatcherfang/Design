# python has no absract class, we use abc to create
from abc import ABCMeta, abstractmethod


class Component(object):
    '''abstract class'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self):
        pass


class Window(Component):
    '''concrete class'''
    def display(self):
        print 'display window'


class TextBox(Component):
    '''concrete class'''
    def display(self):
        print 'display text box'


class ListBox(Component):
    '''concrete class'''
    def display(self):
        print 'display list box'


class ComponentDecorator(Component):
    '''abstract decorator class, attention the parent class Commponent'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def display(self):
        super.display()


class ScrollBarDecorator(ComponentDecorator):
    '''scrollbar concrete decorator class'''
    def __init__(self, component):
        self.component = component

    def display(self):
        self.setScrollBar()
        self.component.display()

    def setScrollBar(self):
        print 'add scrollbar for the component'


class BlackBorderDecorator(ComponentDecorator):
    '''blackboarder concrete decorator class'''
    def __init__(self, component):
        self.component = component

    def display(self):
        self.setBlackBorder()
        self.component.display()

    def setBlackBorder(self):
        print 'set black border for the component'

if __name__ == '__main__':
    print '------------------------------------------'
    component = Window()
    componentSB = ScrollBarDecorator(component)
    componentSB.display()
    print '------------------------------------------'
    componentBB = BlackBorderDecorator(component)
    componentBB.display()
    print '------------------------------------------'
    componentSB_BB = BlackBorderDecorator(componentSB)
    componentSB_BB.display()
    print '------------------------------------------'
