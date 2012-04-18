    
models.py::
    
    class Editorial(models.Model)
        ...
    
    class Group(models.Model):
        editorial = models.ForeignKey(Editorial)
    
    class Link(models.Model):
        group = models.ForeignKey(Group)
        

forms.py::
    
    from nested_formsets.formsets import NestedInlineFormSet
    from nested_formsets.forms import NestedModelForm
        
    class GroupInlineFormSet(NestedInlineFormSet, BaseModelFormSet):
        pass

    class GroupForm(NestedModelForm, forms.ModelForm):
        nested_formset_class = inlineformset_factory(Group, Link)
        class Meta:
            model = Group
            
            
admin.py::
    
    class GroupLinkInline(StackedInline):
        model = Group
        form = GroupForm
        formset = GroupInlineFormSet
    
    class EditorialAdmin(admin.ModelAdmin):
        inlines = (GroupInline,)
        
        

overload admin/edit_inline/fieldset_inline.html and add the code below before the close fieldset tag

    {{ fieldset.form.get_nested_formset.as_p }}