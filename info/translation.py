from modeltranslation.translator import translator, TranslationOptions
from .models import Slider, HomeService, About, Counter, CoreFeature, CoreFeatureVideo, CoreFeatureSection, RenovationInfo, ClientReview, AboutUs, AboutSection, HowItWorks

# Slider Model Translation
class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Slider, SliderTranslationOptions)

# HomeService Model Translation
class HomeServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(HomeService, HomeServiceTranslationOptions)

# About Model Translation
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(About, AboutTranslationOptions)

# Counter Model Translation
class CounterTranslationOptions(TranslationOptions):
    fields = ('label', 'description')

translator.register(Counter, CounterTranslationOptions)

# CoreFeature Model Translation
class CoreFeatureTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(CoreFeature, CoreFeatureTranslationOptions)

# CoreFeatureVideo Model Translation
class CoreFeatureVideoTranslationOptions(TranslationOptions):
    fields = ('video_file', 'thumbnail')

translator.register(CoreFeatureVideo, CoreFeatureVideoTranslationOptions)

# CoreFeatureSection Model Translation
class CoreFeatureSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')

translator.register(CoreFeatureSection, CoreFeatureSectionTranslationOptions)

# RenovationInfo Model Translation
class RenovationInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(RenovationInfo, RenovationInfoTranslationOptions)

# ClientReview Model Translation
class ClientReviewTranslationOptions(TranslationOptions):
    fields = ('section_header', 'reviews_header', 'name', 'position', 'review')

translator.register(ClientReview, ClientReviewTranslationOptions)

# AboutUs Model Translation
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'breadcrumb_title', 'breadcrumb_home')

translator.register(AboutUs, AboutUsTranslationOptions)

# AboutSection Model Translation
class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('main_heading', 'who_we_are_text', 'whats_in_it_for_me_title')

translator.register(AboutSection, AboutSectionTranslationOptions)

# HowItWorks Model Translation
class HowItWorksTranslationOptions(TranslationOptions):
    fields = ('heading_text', 'heading_title', 
              'step_1_title', 'step_1_description',
              'step_2_title', 'step_2_description',
              'step_3_title', 'step_3_description',
              'step_4_title', 'step_4_description')

translator.register(HowItWorks, HowItWorksTranslationOptions)
