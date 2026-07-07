"""
Management command to seed the database with Suraj Mahapatra's portfolio data.
Usage: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from portfolio.models import (
    Profile, SkillCategory, Skill, Experience, ExperienceBullet,
    Project, ProjectBullet, Education, Leadership, LeadershipBullet, Award,
)


class Command(BaseCommand):
    help = 'Seeds the database with portfolio data from resume'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        Profile.objects.all().delete()
        SkillCategory.objects.all().delete()
        Experience.objects.all().delete()
        Project.objects.all().delete()
        Education.objects.all().delete()
        Leadership.objects.all().delete()
        Award.objects.all().delete()

        # ── Profile ──────────────────────────────────────────────
        self.stdout.write('Creating profile...')
        Profile.objects.create(
            full_name='Suraj Mahapatra',
            title='Full-Stack Developer',
            summary=(
                'Full-stack developer with 1+ year building production fintech systems '
                '(React/TypeScript, ASP.NET Core, MongoDB); experienced in OAuth integrations, '
                'async messaging, and scalable API design.'
            ),
            email='surajmahapatra036@gmail.com',
            phone='+91-9304734500',
            location='Jodhpur, India 342001',
            github_url='https://github.com/Suraj6542',
            linkedin_url='https://www.linkedin.com/in/surajmahapatra036/',
            instagram_url='https://instagram.com/_suraj__045',
        )

        # ── Skills ───────────────────────────────────────────────
        self.stdout.write('Creating skills...')

        languages = SkillCategory.objects.create(name='Languages', order=1)
        for name, prof in [
            ('Python', 85), ('C#', 80), ('TypeScript', 85), ('JavaScript', 80),
        ]:
            Skill.objects.create(category=languages, name=name, proficiency=prof)

        frameworks = SkillCategory.objects.create(name='Frameworks', order=2)
        for name, prof in [
            ('ASP.NET Core', 85), ('React', 90), ('Django', 85),
            ('ExpressJS', 75), ('Flask', 70),
        ]:
            Skill.objects.create(category=frameworks, name=name, proficiency=prof)

        databases = SkillCategory.objects.create(name='Databases', order=3)
        for name, prof in [
            ('SQL (MySQL)', 85), ('MongoDB', 80), ('Schema Designing', 75),
        ]:
            Skill.objects.create(category=databases, name=name, proficiency=prof)

        tools = SkillCategory.objects.create(name='Tools', order=4)
        for name, prof in [
            ('Azure DevOps', 50), ('GIT', 90), ('Swagger', 75),
            ('Postman', 85), ('VS Code', 90), ('Visual Studio', 80),
        ]:
            Skill.objects.create(category=tools, name=name, proficiency=prof)

        other = SkillCategory.objects.create(name='Other', order=5)
        for name, prof in [
            ('HTML', 90), ('CSS', 85), ('System Design', 50), ('Agile Methods', 80),
        ]:
            Skill.objects.create(category=other, name=name, proficiency=prof)

        # ── Experience ───────────────────────────────────────────
        self.stdout.write('Creating experience...')

        capsitech = Experience.objects.create(
            company='Capsitech IT Services',
            role='Assistant System Engineer (FullStack Developer)',
            location='',
            start_date='June 2025',
            end_date='Current',
            description='Working under the Acting Office project within the Self Assessment team, handling full-stack development responsibilities across both frontend and backend.',
            order=1,
        )

        bullets_capsitech = [
            {
                'title': 'MTD-IT Module',
                'content': (
                    'Developed from scratch using ASP.NET Core and React + TypeScript, integrating with '
                    "HMRC's Making Tax Digital REST APIs via OAuth 2.0 to enable end-to-end self-assessment "
                    'tax preparation and submission for 200+ users, eliminating manual HMRC filing.'
                ),
                'skills_used': 'ASP.NET Core, React, TypeScript, OAuth 2.0, REST APIs',
                'order': 1,
            },
            {
                'title': 'P11D Data Request Module',
                'content': (
                    'Built with a full expense submission and multi-level admin approval workflow; '
                    'automated P11D return generation post-approval using ASP.NET Core business logic '
                    'and MongoDB aggregation pipelines, reducing manual reconciliation effort by 70%.'
                ),
                'skills_used': 'ASP.NET Core, MongoDB, Aggregation Pipelines',
                'order': 2,
            },
            {
                'title': 'Microsoft Azure',
                'content': (
                    'Worked with Azure Service Bus to process multiple async events/month for event-driven '
                    'processing and Blob Storage for document management in a production environment to '
                    'support scalable payroll and tax workflows.'
                ),
                'skills_used': 'Azure Service Bus, Azure Blob Storage',
                'order': 3,
            },
            {
                'title': 'System Design',
                'content': (
                    'Contributed to HLD and LLD discussions for 2 scalable payroll and tax modules, '
                    'applying microservices patterns, async messaging with Azure Service Bus, and '
                    'RESTful API design principles.'
                ),
                'skills_used': 'System Design, Microservices, Azure Service Bus, REST APIs',
                'order': 4,
            },
        ]
        for b in bullets_capsitech:
            ExperienceBullet.objects.create(experience=capsitech, **b)

        startup_odisha = Experience.objects.create(
            company='Startup Odisha',
            role='Intern',
            location='',
            start_date='September 2023',
            end_date='November 2023',
            description='',
            order=2,
        )

        ExperienceBullet.objects.create(
            experience=startup_odisha,
            title='Data Analysis',
            content=(
                'Managed program datasets and built a Power BI dashboard to analyze '
                'Startup-Yatra and Startup-Xpress outcomes.'
            ),
            skills_used='Power BI, Python, Pandas, NumPy',
            order=1,
        )

        # ── Projects ────────────────────────────────────────────
        self.stdout.write('Creating projects...')

        recall = Project.objects.create(
            title='Recall',
            subtitle='Full-Stack Chrome Extension & Web App',
            description=(
                'Built a full-stack Chrome extension and web app using Django REST Framework '
                'and React that schedules reminders for links, todos, notes, videos, jobs, and purchases.'
            ),
            tech_stack='Django REST Framework, React, MySQL, JWT, Google OAuth',
            github_url='https://github.com/Suraj6542/recall-extension',
            live_url='',
            order=1,
        )

        recall_bullets = [
            {
                'title': 'Authentication',
                'content': (
                    'Implemented secure JWT authentication alongside Google OAuth via the Chrome Identity API, '
                    'verifying tokens on the backend to link accounts and isolate user-specific data.'
                ),
                'order': 1,
            },
            {
                'title': 'Notifications',
                'content': (
                    'Developed a Chrome service worker featuring alarm-based polling, dynamic badges, '
                    'and a stateful notification system that tracks alerts (Pending, Sent, Acknowledged) '
                    'and auto-re-fires dismissed reminders after a 5-minute cooldown.'
                ),
                'order': 2,
            },
            {
                'title': 'UI & Deployment',
                'content': (
                    'Maintained codebase with responsive CSS to support both a full browser view and a compact '
                    '360px popup layout; deployed the backend and MySQL database on Railway, with the extension '
                    'source maintained on GitHub.'
                ),
                'order': 3,
            },
        ]
        for b in recall_bullets:
            ProjectBullet.objects.create(project=recall, **b)

        webscraping = Project.objects.create(
            title='Interview Question Scraper',
            subtitle='Flask Web Scraper',
            description=(
                'Developed a Python Flask scraper to extract interview questions from JavaTpoint and '
                'save the results in multiple formats including MS Word, PDF, and CSV for easy download and review.'
            ),
            tech_stack='Python, Flask, BeautifulSoup, MySQL, CSV, PDF',
            github_url='https://github.com/Suraj6542/Scraping_project.git',
            live_url='',
            order=2,
        )

        webscraping_bullets = [
            {
                'title': 'Data Extraction',
                'content': (
                    'Scraped structured interview questions from a public website and normalized the content into '
                    'a database for reliable querying, filtering, and export.'
                ),
                'order': 1,
            },
            {
                'title': 'Export Formats',
                'content': (
                    'Added export support for DOCX, PDF, and CSV so users can download question sets in their '
                    'preferred format for offline study and sharing.'
                ),
                'order': 2,
            },
        ]
        for b in webscraping_bullets:
            ProjectBullet.objects.create(project=webscraping, **b)

        easy_shop = Project.objects.create(
            title='Easy Shop Platform',
            subtitle='Django E-Commerce Clone',
            description=(
                'Built a user-friendly multi-user e-commerce app with Django, allowing users to register, login, '
                'browse products, add items to cart, place orders, and manage their session flow.'
            ),
            tech_stack='Django, HTML, Bootstrap, MySQL, JavaScript',
            github_url='https://github.com/Suraj6542/Fully_functional_Ecom_application_clone',
            live_url='',
            order=3,
        )

        easy_shop_bullets = [
            {
                'title': 'Shopping Workflow',
                'content': (
                    'Implemented product browsing, cart management, order placement, and checkout workflows '
                    'with clear user feedback and session persistence.'
                ),
                'order': 1,
            },
            {
                'title': 'Auth & UX',
                'content': (
                    'Supported registration, login, logout, and account-specific order history to create a '
                    'realistic multi-user shopping experience.'
                ),
                'order': 2,
            },
        ]
        for b in easy_shop_bullets:
            ProjectBullet.objects.create(project=easy_shop, **b)

        chat_app = Project.objects.create(
            title='Real-Time Chat App',
            subtitle='Django Channels Messaging',
            description=(
                'Created a real-time chat application using Django Channels and WebSockets for '
                'instant communication across authenticated users with independent logouts.'
            ),
            tech_stack='Django, Django Channels, HTML, Bootstrap, WebSockets',
            github_url='https://github.com/Suraj6542/Real_time_chat_app.git',
            live_url='',
            order=4,
        )

        chat_app_bullets = [
            {
                'title': 'Real-Time Messaging',
                'content': (
                    'Built WebSocket-based message delivery with Django Channels to enable chat rooms, '
                    'live typing indicators, and message broadcasting.'
                ),
                'order': 1,
            },
            {
                'title': 'Session Management',
                'content': (
                    'Handled user authentication, independent logout, and real-time session updates to '
                    'keep chats secure and responsive.'
                ),
                'order': 2,
            },
        ]
        for b in chat_app_bullets:
            ProjectBullet.objects.create(project=chat_app, **b)

        # ── Education ────────────────────────────────────────────
        self.stdout.write('Creating education...')

        Education.objects.create(
            institution='Biju Patnaik University of Technology',
            degree='Bachelor of Technology',
            field_of_study='Computer Science & Engineering',
            start_year='2021',
            end_year='2025',
            description='',
            order=1,
        )

        # ── Leadership ───────────────────────────────────────────
        self.stdout.write('Creating leadership...')

        tec = Leadership.objects.create(
            organization='TEC AIC-NALANDA',
            role='Networking Head & Technical Trainee',
            location='Bhubaneswar',
            start_date='Oct 2022',
            end_date='June 2025',
            order=1,
        )

        LeadershipBullet.objects.create(
            leadership=tec,
            title='Networking',
            content=(
                'Led the networking team and collaborated with other college cells '
                'for mini level project development.'
            ),
            order=1,
        )
        LeadershipBullet.objects.create(
            leadership=tec,
            title='Training',
            content=(
                'Conducted doubt clearing sessions to resolve technical queries for students.'
            ),
            order=2,
        )

        # ── Awards ───────────────────────────────────────────────
        self.stdout.write('Creating awards...')

        Award.objects.create(
            title='Won the Database Management Competition at the BPUT Tech Carnival',
            description='Competed and won first place in the Database Management Competition.',
            date='December 2024',
            order=1,
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
