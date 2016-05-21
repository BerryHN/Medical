init python:

    class Input(renpy.text.text.Text): #@UndefinedVariable
        """
        This is a Displayable that takes text as input.
        """
    
        changed = None
        prefix = ""
        suffix = ""
        caret_pos = 0
        
        def __init__(self,
                     default="",
                     length=None,
                     style='input',
                     allow=None,
                     exclude=None,
                     prefix="",
                     suffix="",
                     changed=None,
                     button=None,
                     replaces=None,
                     editable=True,
                     result_checker=None,
                     **properties):
    
            super(Input, self).__init__("", style=style, replaces=replaces, substitute=False, **properties)
    
            self.content = unicode(default)
            self.length = length
    
            self.allow = allow
            self.exclude = exclude
            self.prefix = prefix
            self.suffix = suffix
    
            self.changed = changed
    
            self.editable = editable

            caretprops = { 'color' : None }
            
            for i in properties:
                if i.endswith("color"):
                    caretprops[i] = properties[i]

            self.result_checker = result_checker   
            self.good_color = self.style.color
            self.bad_color = "#f00"
            self.is_input_good = True
    
            self.caret = Animation(
                    renpy.display.image.Solid(xmaximum=1, style=style, **caretprops), 0.5,
                    renpy.display.image.Solid(xmaximum=1, style=style, color=(0,0,0,0)), 0.5
                )
            self.caret_pos = len(self.content)
    
            if button:
                self.editable = False
                button.hovered = HoveredProxy(self.enable, button.hovered)
                button.unhovered = HoveredProxy(self.disable, button.unhovered)
    
            if isinstance(replaces, Input):
                self.content = replaces.content
                self.editable = replaces.editable
                self.caret_pos = replaces.caret_pos
    
            self.update_text(self.content, self.editable)
    
    
        def update_text(self, content, editable):
    
            if content != self.content or editable != self.editable:
                renpy.display.render.redraw(self, 0)
                                                
            if content != self.content:
                self.content = content
    
                if self.changed:
                    self.changed(content)
                    
            if content == "":
                content = u"\u200b"
                    
            self.editable = editable
    
            # Choose the caret.
            caret = self.style.caret
            if caret is None:
                caret = self.caret
                                                
            if editable:
                l = len(content)
                self.set_text([self.prefix, content[0:self.caret_pos].replace("{", "{{"), caret,
                                            content[self.caret_pos:l].replace("{", "{{"), self.suffix])
            else:
                self.set_text([self.prefix, content.replace("{", "{{"), self.suffix ])
    
        # This is needed to ensure the caret updates properly.
        def set_style_prefix(self, prefix, root):
            if prefix != self.style.prefix:
                self.update_text(self.content, self.editable)
    
            super(Input, self).set_style_prefix(prefix, root)
    
        def enable(self):
            self.update_text(self.content, True)
    
        def disable(self):
            self.update_text(self.content, False)
                
        def event(self, ev, x, y, st):
            import pygame
    
            if not self.editable:
                return None
            
            l = len(self.content)

            if not self.is_input_good:
                self.is_input_good = True
                self.style.__setstate__({'color':self.good_color})

            
            if renpy.display.behavior.map_event(ev, "input_backspace"):
    
                if self.content and self.caret_pos > 0:
                    content = self.content[0:self.caret_pos-1] + self.content[self.caret_pos:l]
                    self.caret_pos -= 1
                    self.update_text(content, self.editable)
                                                
                renpy.display.render.redraw(self, 0)
                raise renpy.display.core.IgnoreEvent()
    
            elif renpy.display.behavior.map_event(ev, "input_enter"):
                if not self.changed:
                    if  not self.result_checker or self.result_checker(self.content):
                        return self.content
                    else:
                        self.is_input_good = False
                        self.style.__setstate__({'color':self.bad_color})
                        self.update_text(self.content, self.editable)
                        renpy.display.render.redraw(self, 0)
                        raise renpy.display.core.IgnoreEvent()
    
            elif renpy.display.behavior.map_event(ev, "input_left"):
                if self.caret_pos > 0:
                    self.caret_pos -= 1
                    self.update_text(self.content, self.editable)
                                                
                renpy.display.render.redraw(self, 0)
                raise renpy.display.core.IgnoreEvent()
    
            elif renpy.display.behavior.map_event(ev, "input_right"):
                if self.caret_pos < l:
                    self.caret_pos += 1
                    self.update_text(self.content, self.editable)
                                                
                renpy.display.render.redraw(self, 0)
                raise renpy.display.core.IgnoreEvent()
    
            elif renpy.display.behavior.map_event(ev, "input_delete"):
                if self.caret_pos < l:
                    content = self.content[0:self.caret_pos] + self.content[self.caret_pos+1:l]
                    self.update_text(content, self.editable)
                                                
                renpy.display.render.redraw(self, 0)
                raise renpy.display.core.IgnoreEvent()
    
            elif ev.type == pygame.KEYDOWN and ev.unicode:
                if ord(ev.unicode[0]) < 32:
                    return None
                    
                if self.length and len(self.content) >= self.length:
                    raise renpy.display.core.IgnoreEvent()
    
                if self.allow and ev.unicode not in self.allow:
                    raise renpy.display.core.IgnoreEvent()
    
                if self.exclude and ev.unicode in self.exclude:
                    raise renpy.display.core.IgnoreEvent()
    
                content = self.content[0:self.caret_pos] + ev.unicode + self.content[self.caret_pos:l]
                self.caret_pos += 1
    
                self.update_text(content, self.editable)
    
                raise renpy.display.core.IgnoreEvent()


    def input_text_wrapper(default, length=None, allow=None, exclude='{}', **properties):
        return ui.add(Input(default, length=length, allow=allow, exclude=exclude, **properties))

    renpy.ui.input = input_text_wrapper