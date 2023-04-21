from django.core.management.base import BaseCommand
from inventory.models import Province, District, Ward
from inventory.serializers import ProvinceSerializer, DistrictSerializer, WardSerializer
from django.templatetags.static import static
import json
class Command(BaseCommand):
    help = 'Import provinces from xlsx'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('inventory/{}'.format(static("provinces.json")),encoding='utf-8') as file:
            provinces = json.load(file)
        for province in provinces:
            print('creating province {}'.format(province['name']))
            if not Province.objects.filter(name=province["name"]).exists():
                province_row = Province.objects.create(name=province["name"])
                province_row.save()
            for district in province['districts']:
                print('creating district {}'.format(district['name']))
                province_row = Province.objects.filter(name=province["name"]).first()
                if not District.objects.filter(name=district["name"]).exists():
                    district_row = District.objects.create(name=district["name"], province=province_row)
                    district_row.save()
                for ward in district['wards']:
                    print('creating ward {}'.format(ward['name']))
                    district_row = District.objects.filter(name=district["name"]).first()
                    if not Ward.objects.filter(name=ward["name"]).exists():
                        ward_row = Ward.objects.create(name=ward["name"], district=district_row)
                        ward_row.save()