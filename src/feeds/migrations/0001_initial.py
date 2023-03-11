# Generated by Django 4.1.7 on 2023-03-13 19:46

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import feeds.models.article
import feeds.models.feed
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the author",
                        max_length=100,
                        verbose_name="Name",
                    ),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        help_text="The slug uniquely identifying the author",
                        max_length=100,
                        populate_from="name",
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="A short profile of the author",
                        verbose_name="Description",
                    ),
                ),
            ],
            options={
                "verbose_name": "Author",
                "verbose_name_plural": "Authors",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("slug", models.SlugField()),
                (
                    "count",
                    models.IntegerField(
                        default=0,
                        help_text="Internal counter of how many times this tag is in use",
                    ),
                ),
                (
                    "protected",
                    models.BooleanField(
                        default=False,
                        help_text="Will not be deleted when the count reaches 0",
                    ),
                ),
                ("path", models.TextField()),
                (
                    "label",
                    models.CharField(
                        help_text="The name of the tag, without ancestors",
                        max_length=255,
                    ),
                ),
                (
                    "level",
                    models.IntegerField(
                        default=1, help_text="The level of the tag in the tree"
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="feeds.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
            bases=(tagulous.models.models.BaseTagTreeModel, models.Model),
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the source",
                        max_length=100,
                        verbose_name="Name",
                    ),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        help_text="The slug uniquely identifying the source",
                        max_length=100,
                        populate_from="name",
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True,
                        help_text="The URL for source's web site",
                        verbose_name="Web site",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="A description of the source",
                        verbose_name="Description",
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Data describing a source",
                        verbose_name="Data",
                    ),
                ),
            ],
            options={
                "verbose_name": "Source",
                "verbose_name_plural": "Sources",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="",
                        help_text="The name of the tag",
                        max_length=100,
                        verbose_name="Name",
                    ),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        help_text="The slug uniquely identifying the tag",
                        max_length=100,
                        populate_from="name",
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "summary",
                    models.TextField(
                        blank=True,
                        help_text="A short summary of what the tag covers",
                        verbose_name="Summary",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="A more detailed description of the tag. May be in HTML",
                        verbose_name="Description",
                    ),
                ),
                (
                    "related",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The set of tag(s) that are related to this one",
                        to="feeds.tag",
                        verbose_name="Related tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="Feed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the feed",
                        max_length=100,
                        verbose_name="Name",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="The URL for the RSS feed (RSS or Atom)",
                        verbose_name="URL",
                    ),
                ),
                (
                    "enabled",
                    models.BooleanField(
                        default=False,
                        help_text="Enable loading of the RSS feed",
                        verbose_name="Enabled",
                    ),
                ),
                (
                    "schedule",
                    models.CharField(
                        blank=True,
                        help_text="Crontab entry which describe the times the feed will be downloaded.Leave blank to use the default schedule defined for all feeds.",
                        max_length=100,
                        validators=[feeds.models.feed.validate_crontab],
                        verbose_name="Schedule",
                    ),
                ),
                (
                    "auto_publish",
                    models.BooleanField(
                        default=False,
                        help_text="Automatically publish Articles when added from an RSS Feed",
                        verbose_name="Auto Publish",
                    ),
                ),
                (
                    "loaded",
                    models.DateTimeField(
                        blank=True,
                        help_text="The date that the RSS feed was last loaded",
                        null=True,
                        verbose_name="Loaded",
                    ),
                ),
                (
                    "failures",
                    models.IntegerField(
                        default=0,
                        help_text="The number of consecutive times a feed has failed to load.",
                        verbose_name="Failures",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        blank=True,
                        help_text="The HTTP status code from the last time the feed was fetched",
                        null=True,
                        verbose_name="Status",
                    ),
                ),
                (
                    "etag",
                    models.CharField(
                        blank=True,
                        help_text="The Etag header from the RSS feed (Atom feeds only)",
                        max_length=100,
                        null=True,
                        verbose_name="ETag",
                    ),
                ),
                (
                    "last_modified",
                    models.DateTimeField(
                        blank=True,
                        help_text="The last-modified header from the RSS feed",
                        null=True,
                        verbose_name="Last Modified",
                    ),
                ),
                (
                    "categories",
                    tagulous.models.fields.TagField(
                        _set_tag_meta=True,
                        blank=True,
                        force_lowercase=True,
                        help_text="The categories of articles published by the feed",
                        to="feeds.category",
                        tree=True,
                        verbose_name="Categories",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        help_text="The web site which hosts the feed",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="feeds.source",
                        verbose_name="Source",
                    ),
                ),
            ],
            options={
                "verbose_name": "Feed",
                "verbose_name_plural": "Feeds",
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="The title of the article",
                        max_length=1000,
                        verbose_name="Title",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="The link to the article on the source's web site",
                        max_length=2000,
                        verbose_name="URL",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        default=feeds.models.article.article_code,
                        help_text="The code that used to identify the article",
                        max_length=6,
                        verbose_name="Code",
                    ),
                ),
                (
                    "archive_url",
                    models.URLField(
                        blank=True,
                        help_text="The link to the archived article using a service such as archive.today",
                        max_length=2000,
                        verbose_name="Archive URL",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        help_text="The date the article was published by the source",
                        verbose_name="Date",
                    ),
                ),
                (
                    "summary",
                    models.TextField(
                        blank=True,
                        help_text="A summary of the article",
                        verbose_name="Summary",
                    ),
                ),
                (
                    "identifier",
                    models.CharField(
                        blank=True,
                        help_text="The unique identifier for the Article from the Feed",
                        max_length=2000,
                        verbose_name="Identifier",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="An editorial comment about the article",
                        verbose_name="Comment",
                    ),
                ),
                (
                    "publish",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        help_text="Publish the article on the site",
                        verbose_name="Publish",
                    ),
                ),
                (
                    "views",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="The number of times the article has been viewed (read)",
                        verbose_name="Views",
                    ),
                ),
                (
                    "data",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Data describing an article",
                        verbose_name="Data",
                    ),
                ),
                (
                    "authors",
                    models.ManyToManyField(
                        help_text="The author(s) who wrote the article",
                        related_name="articles",
                        to="feeds.author",
                        verbose_name="Authors",
                    ),
                ),
                (
                    "categories",
                    tagulous.models.fields.TagField(
                        _set_tag_meta=True,
                        blank=True,
                        help_text="The categories that describes the article contents",
                        to="feeds.category",
                        tree=True,
                        verbose_name="Categories",
                    ),
                ),
                (
                    "feed",
                    models.ForeignKey(
                        blank=True,
                        help_text="The feed from the host web site",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="articles",
                        to="feeds.feed",
                        verbose_name="RSS Feed",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        help_text="The source (blog, news site, etc.) which published the article",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="articles",
                        to="feeds.source",
                        verbose_name="Source",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Keywords for subjects covered in the content",
                        to="feeds.tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
                "get_latest_by": "date",
            },
        ),
        migrations.CreateModel(
            name="Alias",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="A name used to lookup an author from a feed entry",
                        max_length=100,
                        verbose_name="Name",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="The Author that the feed entry author maps to",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="aliases",
                        to="feeds.author",
                        verbose_name="Author",
                    ),
                ),
                (
                    "feed",
                    models.ForeignKey(
                        help_text="The feed where the alias is used",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="feeds.feed",
                        verbose_name="Feed",
                    ),
                ),
            ],
            options={
                "verbose_name": "Alias",
                "verbose_name_plural": "Aliases",
            },
        ),
    ]
