import warnings
try:
    from modeltranslation.translator import translator, TranslationOptions
    from schedule.models.events import Event, Occurrence


    class TitleDescriptionTranslationOptions(TranslationOptions):
        fields = ('title', 'description', )

    translator.register(Event, TitleDescriptionTranslationOptions)
    translator.register(Occurrence, TitleDescriptionTranslationOptions)
except Exception as exc:
    warnings.warn("translations not installed")
