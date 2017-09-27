from django.shortcuts import render

from cms.plugin_base import CMSPluginBase

from .models import Category, Menu

class Custom_menu_data(CMSPluginBase):
    def get(set_pk):
        c = []
        menus = []
        dicc_menu = []
        dicc_category = []
        dicc_banner = []
        dicc_pages = []
        dicc_page = []
        dicc_subpages = []
        Dicc = {}

        pk = set_pk
        M = Menu.objects.get(pk=pk)

        id_menu = M.pk
        Name_menu = M.name
        Titel_menu = M.titel
        menu = {
                'id_menu' : id_menu,
                'Name_menu' : Name_menu,
                'Titel_menu' : Titel_menu,
            }
        for l in M.category.all():
            id_Categoria = l.pk
            Name_Category = l.name
            Titel_Category = l.titel
            Level_Category = l.Level
            URL_Category = l.url

            category = {
                        'id_Categoria' : id_Categoria,
                        'Name_Category' : Name_Category,
                        'Titel_Category' : Titel_Category,
                        'Level_Category' : Level_Category,
                        'URL_Category' : URL_Category,
                        }

            for m in l.Banner.all():
                id_Categoria = l.pk
                Banner_name = m.name
                Banner_URL = m.url
                Banner_Image = m.Imagen.url
                Banner = {
                             'id_Categoria' : id_Categoria,
                             'Banner_name': Banner_name,
                             'Banner_URL' : Banner_URL,
                             'Banner_Image' : Banner_Image,
                             }

                dicc_banner.append(Banner)
            Dicc_banner = { 'Banner' : dicc_banner, }
            dicc_banner = []
            category.update(Dicc_banner)
            dicc_category.append(category)

            for s in l.Pages.all():
                ids_pages = s.pk
                id_Categoria = l.pk
                Titel_Pages = s.titel
                Name_Pages = s.name
                pages = {
                        'id_Categoria' : id_Categoria,
                        'ids_pages' : ids_pages,
                        'Name_Pages' : Name_Pages,
                        'Titel_Pages' : Titel_Pages,
                        }

                for h in s.page.all():
                    id_Categoria = l.pk
                    id_pages = s.pk
                    id_page = h.pk
                    Titel_Page = h.page_external.get_page_title()
                    Titel_external = h.titel
                    Name_Page = h.name
                    URL_Page = h.page_external.get_absolute_url()
                    URL_external = h.url
                    Icon_Page = h.Icon
                    Position_X_Icon = h.X
                    Position_Y_Icon = h.Y
                    Page = h.page_external
                    page =  {
                            'id_Categoria' : id_Categoria,
                            'id_pages' : id_pages,
                            'id_page' : id_page,
                            'Titel_Pages' : Titel_Pages,
                            'Titel_external' : Titel_external,
                            'URL_Page' : URL_Page,
                            'URL_external' : URL_external,
                            'Icon_Page' : Icon_Page,
                            'Position_X_Icon' : Position_X_Icon,
                            'Position_Y_Icon' : Position_Y_Icon,
                            }
                    for b in h.subpages.all():
                        id_Categoria = l.pk
                        id_page = h.pk
                        id_subpages = b.pk
                        Titel_subpages = b.Pages_external.get_page_title()
                        Titel_external_subpages = b.titel
                        Name_subpages = b.name
                        URL_subpages = b.Pages_external.get_absolute_url()
                        URL_external_subpages = b.url
                        subPage = Pages_external
                        subpages =  {
                                    'id_Categoria' : id_Categoria,
                                    'id_page' : id_page,
                                    'id_subpages' : id_subpages,
                                    'Titel_subpages' : Titel_subpages,
                                    'Titel_external_subpages' : Titel_external_subpages,
                                    'URL_subpages' : URL_subpages,
                                    'URL_external_subpages' : URL_external_subpages,
                                    }
                        dicc_subpages.append(subpages)
                    Dicc_subpages = { 'SubPages' : dicc_subpages, }
                    dicc_subpages = []
                    page.update(Dicc_subpages)
                    dicc_page.append(page)
                Dicc_page = { 'Page' : dicc_page, }
                dicc_page = []
                pages.update(Dicc_page)
                dicc_pages.append(pages)
            Dicc_Pages = { 'Pages' : dicc_pages, }
            dicc_pages = []
            category.update(Dicc_Pages)
        Dicc_category = { 'Category' : dicc_category, }
        dicc_category = []
        menu.update(Dicc_category)
        dicc_menu.append(menu)

        c = dicc_menu
        return c
