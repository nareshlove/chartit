from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from chartit import DataPool, Chart
from .models import MonthlyWeatherByCity


def index(request):
    return render(request, "index.html")


def download(request):
    return render(request, "download.html")


def about(request):
    return render(request, "about.html")


class LineChartView(TemplateView):
    template_name = 'core/linechart.html'

    def get_ds(self):
        return DataPool(
            series=[{'options': {
                'source': MonthlyWeatherByCity.objects.all()},
                'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
            ])

    def get_water_chart(self):
        return Chart(
            datasource=self.get_ds(),
            series_options=[{'options': {
                'type': 'line',
                'stacking': False},
                'terms': {
                'month': [
                    'boston_temp',
                    'houston_temp']
            }}],
            chart_options={'title': {
                'text': 'Weather Data of Boston and Houston'},
                'xAxis': {
                'title': {
                    'text': 'Month number'}}})

    def get_context_data(self, **kwargs):
        context = super(MyTemplateView, self).get_context_data(**kwargs)
        context['weatherchart'] = self.get_water_chart()

        return context


def piechart(request):
    ds = DataPool(
        series=[{'options': {
            'source': MonthlyWeatherByCity.objects.all()},
            'terms': [
            'month',
            'boston_temp']}
        ])

    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]

    cht = Chart(
        datasource=ds,
        series_options=[{'options': {
            'type': 'pie',
            'stacking': False},
            'terms': {
            'month': [
                'boston_temp']
        }}],
        chart_options={'title': {
            'text': 'Monthly Temperature of Boston'}},
        x_sortf_mapf_mts=(None, monthname, False))

    return render_to_response('core/piechart.html', {'weatherchart': cht})


def multiplechart(request):
    ds = DataPool(
        series=[{'options': {
            'source': MonthlyWeatherByCity.objects.all()},
            'terms': [
            'month',
            'houston_temp',
                'boston_temp']}])

    cht = Chart(
        datasource=ds,
        series_options=[{'options': {
            'type': 'line',
            'xAxis': 0,
            'yAxis': 0,
            'zIndex': 1},
            'terms': {
            'month': [
                'boston_temp']}},
            {'options': {
             'type': 'area',
             'xAxis': 1,
             'yAxis': 1},
             'terms': {
             'month': ['houston_temp']}}],
        chart_options={'title': {
            'text': 'Weather Data by Month (on different axes)'},
            'xAxis': {
            'title': {
                'text': 'Month number'}}})
    return render_to_response('core/multiplechart.html', {'weatherchart': cht})


def combinationchart(request):
    ds = DataPool(
        series=[{'options': {
            'source': MonthlyWeatherByCity.objects.all()},
            'terms': [
            'month',
            'boston_temp',
            'houston_temp']}
        ])

    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]

    cht = Chart(
        datasource=ds,
        series_options=[{'options': {
            'type': 'line'},
            'terms': {
            'month': [
                'boston_temp']
        }},
            {'options': {
             'type': 'pie',
             'center': [150, 100],
             'size': '50%'},
             'terms':{
                'month': [
                    'houston_temp']
            }}],
        chart_options={'title': {
            'text': 'Weather Data of Boston (line) and Houston (pie)'}},
        x_sortf_mapf_mts=[(None, monthname, False),
                          (None, monthname, False)])
    return render_to_response('core/multiplechart.html', {'weatherchart': cht})

# http://stackoverflow.com/a/25839210/802542
# http://stackoverflow.com/questions/30405236/transform-function-view-in-class-based-view-django-chartit
