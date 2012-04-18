class NestedModelForm(object):
    nested_formset_class = None
    def __init__(self, **kwargs):
        super(NestedModelForm, self).__init__(**kwargs)
        self._nested_formset = None
    
    def set_instance(self, instance):
        self.instance = instance
        self._nested_formset = None
    
    def get_nested_formset(self, *args, **kwargs):
        
        if self._nested_formset is None:
            self._nested_formset = self.nested_formset_class(instance=self.instance, 
                                        prefix=self.prefix,  *args, **kwargs)
            
        return self._nested_formset