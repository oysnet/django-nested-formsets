from django.core.exceptions import ValidationError
from django.db.models.deletion import PROTECT
class NestedInlineFormSet(object):
    
    @property
    def nested_formsets(self):
        # iter over existing forms
        for form in self.initial_forms:
            yield form.get_nested_formset(data=self.data, files=self.files)
        
        # used to retrieve newly created objects in self.new_objects
        counter = 0
        
        # iter over new forms
        for form in self.extra_forms:
            if not form.has_changed():
                continue
            
            # new_objects attribute does not exist when validating 
            if hasattr(self, 'new_objects'):
                form.set_instance(self.new_objects[counter])
                counter += 1
            yield form.get_nested_formset(data=self.data, files=self.files)
    
    def clean(self, *args, **kwargs):
        
        super(NestedInlineFormSet, self).clean(*args, **kwargs)
        for form in self.initial_forms:
            if self._should_delete_form(form):
                nested_formset = form.get_nested_formset(data=self.data, files=self.files)
                has_children = len(nested_formset.initial_forms) > 0
                
                if has_children and nested_formset.fk.rel.on_delete == PROTECT:
                    raise ValidationError('Deleting a %s with %s is not allowed' % (nested_formset.fk.verbose_name, nested_formset.fk.model._meta.verbose_name))
        
        
    def is_valid(self):
        
        valid = super(NestedInlineFormSet, self).is_valid()
        
        for nested_formset in self.nested_formsets:
            valid = valid and nested_formset.is_valid()
            
        return valid
    
    def save(self, commit=True):
        objects = super(NestedInlineFormSet, self).save(commit)
        for nested_formset in self.nested_formsets:
            
            if hasattr(self, 'deleted_objects') and nested_formset.instance in self.deleted_objects:
                continue
            else:
                nested_formset.save(commit)
        
        return objects