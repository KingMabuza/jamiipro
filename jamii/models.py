from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    description = models.CharField(max_length=255)
    body = RichTextField()
    date_posted = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.title


class Exporter(models.Model):
    Type_of_Export = (
                         ('Live Animals', 'Live Animals'),
                         ('Meat and edible meat offal', 'Meat and edible meat offal'),
                         ('Fish and crustaceans, molluscs and other aquatic invertebrates',
                          'Fish and crustaceans, molluscs and other '
                          'aquatic invertebrates'),
                         (
                             'Dairy produce; birds eggs; natural honey; edible products of animal origin, '
                             'not elsewhere specified or '
                             'included',
                             'Dairy produce; birds eggs; natural honey; edible products of animal origin, '
                             'not elsewhere '
                             'specified or included'),
                         ('Live trees and other plants; bulbs, roots and the like; cut flowers and ornamental foliage',
                          'Live trees '
                          'and other '
                          'plants; '
                          'bulbs, '
                          'roots and the '
                          'like; cut '
                          'flowers and '
                          'ornamental '
                          'foliage'),
                         ('Edible vegetables and certain roots and tubers',
                          'Edible vegetables and certain roots and tubers'),
                         ('Edible fruit and nuts; peel of citrus fruit or melons',
                          'Edible fruit and nuts; peel of citrus fruit or '
                          'melons'),
                         ('Coffee, tea, maté and spices', 'Coffee, tea, maté and spices'),
                         ('Cereals', 'Cereals'),
                         ('Products of the milling industry; malt; starches; inulin; wheat gluten',
                          'Products of the milling industry; '
                          'malt; starches; inulin; wheat '
                          'gluten'),
                         (
                             'Oil seeds and oleaginous fruits; miscellaneous grains, seeds and fruit; industrial or '
                             'medicinal plants; '
                             'straw and fodder',
                             'Oil seeds and oleaginous fruits; miscellaneous grains, seeds and fruit; industrial or '
                             'medicinal plants; straw and fodder'),
                         ('Lac; gums, resins and other vegetable saps and extracts',
                          'Lac; gums, resins and other vegetable saps and '
                          'extracts'),
                         ('Vegetable plaiting materials; vegetable products not elsewhere specified or included',
                          'Vegetable plaiting '
                          'materials; '
                          'vegetable products '
                          'not elsewhere '
                          'specified or '
                          'included'),
                         (
                             'Animal or vegetable fats and oils and their cleavage products; prepared edible fats; '
                             'animal '
                             'or vegetable '
                             'waxes',
                             'Animal or vegetable fats and oils and their cleavage products; prepared edible fats; '
                             'animal or '
                             'vegetable waxes'),
                         ('Preparations of meat, of fish or of crustaceans, molluscs or other aquatic invertebrates',
                          'Preparations of '
                          'meat, '
                          'of fish or of '
                          'crustaceans, '
                          'molluscs or '
                          'other aquatic '
                          'invertebrates'),
                         ('Sugars and sugar confectionery', 'Sugars and sugar confectionery'),
                         ('Cocoa and cocoa preparations', 'Cocoa and cocoa preparations'),
                         ('Preparations of cereals, flour, starch or milk; pastrycooks products',
                          'Preparations of cereals, flour, '
                          'starch or milk; pastrycooks '
                          'products'),
                         ('Preparations of vegetables, fruit, nuts or other parts of plants',
                          'Preparations of vegetables, fruit, nuts '
                          'or other parts of plants'),
                         ('Miscellaneous edible preparations', 'Miscellaneous edible preparations'),
                         ('Beverages, spirits and vinegar', 'Beverages, spirits and vinegar'),
                         ('Residues and waste from the food industries; prepared animal fodder',
                          'Residues and waste from the food '
                          'industries; prepared animal fodder'),
                         ('Tobacco and manufactured tobacco substitutes',
                          'Tobacco and manufactured tobacco substitutes'),
                         ('Salt; sulphur; earths and stone; plastering materials, lime and cement', 'Salt; sulphur; '
                                                                                                    'earths and '
                                                                                                    'stone; '
                                                                                                    'plastering '
                                                                                                    'materials, '
                                                                                                    'lime and cement'),
                         ('Ores, slag and ash', 'Ores, slag and ash'),
                         ('Mineral fuels, mineral oils and products of their distillation; bituminous substances; '
                          'mineral waxes', 'Mineral fuels, mineral oils and products of their distillation; '
                                           'bituminous substances; mineral waxes'),
                         ('Inorganic chemicals; organic or inorganic compounds of precious metals, of rare-earth '
                          'metals, of radioactive elements or of isotopes', 'Inorganic chemicals; organic or '
                                                                            'inorganic compounds of precious '
                                                                            'metals, of rare-earth metals, '
                                                                            'of radioactive elements or of isotopes'),
                         ('Organic chemicals', 'Organic chemicals'),
                         ('Pharmaceutical products', 'Pharmaceutical products'),
                         ('Fertilisers', 'Fertilisers'),
                         ('Tanning or dyeing extracts; tannins and their derivatives; dyes, pigments and other '
                          'colouring matter; paints and varnishes; putty and other mastics; inks', 'Tanning or dyeing '
                                                                                                   'extracts; tannins '
                                                                                                   'and their '
                                                                                                   'derivatives; '
                                                                                                   'dyes, '
                                                                                                   'pigments and '
                                                                                                   'other colouring '
                                                                                                   'matter; paints '
                                                                                                   'and varnishes; '
                                                                                                   'putty and other '
                                                                                                   'mastics; inks'),
                         ('Essential oils and resinoids; perfumery, cosmetic or toilet preparations', 'Essential oils '
                                                                                                      'and resinoids;'
                                                                                                      ' perfumery, '
                                                                                                      'cosmetic or '
                                                                                                      'toilet '
                                                                                                      'preparations'),
                         ('Soap, organic surface-active agents, washing preparations, lubricating preparations, '
                          'artificial waxes, prepared waxes, polishing or scouring preparations, candles and similar '
                          'articles, modelling pastes, «dental waxes» and dental preparations with a basis of '
                          'plaster', 'Soap, organic surface-active agents, washing preparations, lubricating '
                                     'preparations, artificial waxes, prepared waxes, polishing or scouring '
                                     'preparations, candles and similar articles, modelling pastes, «dental waxes» '
                                     'and dental preparations with a basis of plaster'),
                         ('Albuminoidal substances; modified starches; glues; enzymes', 'Albuminoidal substances; '
                                                                                        'modified starches; glues; '
                                                                                        'enzymes'),
                         ('Explosives; pyrotechnic products; matches; pyrophoric alloys; certain combustible '
                          'preparations', 'Explosives; pyrotechnic products; matches; pyrophoric alloys; certain '
                                          'combustible preparations'),
                         ('Photographic or cinematographic goods', 'Photographic or cinematographic goods'),
                         ('Miscellaneous chemical products', 'Miscellaneous chemical products'),
                         ('Plastics and articles thereof', 'Plastics and articles thereof'),
                         ('Rubber and articles thereof', 'Rubber and articles thereof'),
                         ('Raw hides and skins (other than furskins) and leather', 'Raw hides and skins (other than '
                                                                                   'furskins) and leather'),
                         ('Articles of leather; saddlery and harness; travel goods, handbags and similar containers; '
                          'articles of animal gut (other than silk-worm gut)', 'Articles of leather; saddlery and '
                                                                               'harness; travel goods, handbags and '
                                                                               'similar containers; articles of '
                                                                               'animal gut (other than silk-worm gut)'),
                         ('Furskins and artificial fur; manufactures thereof', 'Furskins and artificial fur; '
                                                                               'manufactures thereof'),
                         ('Wood and articles of wood; wood charcoal', 'Wood and articles of wood; wood charcoal'),
                         ('Cork and articles of cork', 'Cork and articles of cork'),
                         ('Manufactures of straw, of esparto or of other plaiting materials; basketware and wickerwork',
                          'Manufactures of straw, of esparto or of other plaiting materials; basketware and wickerwork'),
                         ('Pulp of wood or of other fibrous cellulosic material; recovered (waste and scrap) paper or '
                          'paperboard', 'Pulp of wood or of other fibrous cellulosic material; recovered (waste and '
                                        'scrap) paper or paperboard'),
                         ('Paper and paperboard; articles of paper pulp, of paper or of paperboard', 'Paper and '
                                                                                                     'paperboard; '
                                                                                                     'articles of '
                                                                                                     'paper pulp, '
                                                                                                     'of paper or of '
                                                                                                     'paperboard'),
                         ('Printed books, newspapers, pictures and other products of the printing industry; '
                          'manuscripts, typescripts and plans', 'Printed books, newspapers, pictures and other '
                                                                'products of the printing industry; manuscripts, '
                                                                'typescripts and plans'),
                         ('Printed books, newspapers, pictures and other products of the printing industry; '
                          'manuscripts, typescripts and plans', 'Printed books, newspapers, pictures and other '
                                                                'products of the printing industry; manuscripts, '
                                                                'typescripts and plans'),
                     )

    List_of_Country = (
        ('Angola', 'Angola'),
        ('Botswana', 'Botswana'),
        ('Comoros', 'Comoros'),
        ('Democratic Republic of Congo', 'Democratic Republic of Congo'),
        ('Eswatini', 'Eswatini'),
        ('Madagascar', 'Madagascar'),
        ('Malawi', 'Malawi'),
        ('Mauritius', 'Mauritius'),
        ('Mozambique', 'Mozambique'),
        ('Namibia', 'Namibia'),
        ('Seychelles', 'Seychelles'),
        ('South Africa', 'South Africa'),
        ('Tanzania', 'Tanzania'),
        ('Zambia', 'Zambia'),
        ('Zimbabwe', 'Zimbabwe')
    )
    Export_Industry = models.TextField(max_length=500, choices=Type_of_Export, blank=True)
    Export_From = models.TextField(max_length=500, choices=List_of_Country, blank=True)
    Export_To = models.TextField(max_length=500, choices=List_of_Country, blank=True)
    Export_Domestic_Requirements = RichTextField(null=True)
    Export_Product_Requirements = RichTextField(null=True)
    Export_Market_Conditions = RichTextField(null=True)
    Export_preShipment_Inspection = RichTextField(null=True)
    Export_Tariff = RichTextField(null=True)
    Export_Taxes = RichTextField(null=True)
    Export_TradePartner = RichTextField(null=True)

    def __str__(self):
        return self.Export_Industry


class Glossary(models.Model):
    name = models.CharField(max_length=255)
    meaning = models.TextField(null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    date = models.DateTimeField(default=timezone.now)
    description = RichTextField(null=True)
    location = models.CharField(max_length=255)
    booking_url = models.URLField(null=True)
    event_cover = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
        return self.name
