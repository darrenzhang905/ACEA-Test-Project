# -*- coding: utf-8 -*-
import scrapy
from ..items import OnlineCoursesItem

class OnlineCourseSpider(scrapy.Spider):
    name = 'online_courses'
    start_urls = ['http://onlinecourses.com/accounting/']
    all_subjects = ['accounting', 'computerscience', 'criminal-justice', 'education', 'healthcare', 'humanities',
                    'information-technology', 'language', 'math', 'physics', 'science', 'statistics', 'teaching']
    num_subjects = 13
    curr_subject = 0

    def parse(self, response):
        subject = OnlineCourseSpider.all_subjects[OnlineCourseSpider.curr_subject]
        num_courses = len(response.css('section header hgroup h2::text').extract())
        items = OnlineCoursesItem()

        for i in range(num_courses):
            course_name = response.css('section header hgroup h2::text')[i].extract().strip()
            tags = response.css('section header span.tags::text')[i].extract().strip()
            url = response.css('#coursewares li + li a::attr(href)')[i].extract().strip()

            items['subject'] = subject
            items['course_name'] = course_name
            items['tags'] = tags
            items['url'] = url

            yield items

        OnlineCourseSpider.curr_subject += 1
        next_page = 'http://onlinecourses.com/' + str(OnlineCourseSpider.all_subjects[OnlineCourseSpider.curr_subject]) + '/'

        if OnlineCourseSpider.curr_subject < OnlineCourseSpider.num_subjects:
            yield response.follow(next_page, callback = self.parse)