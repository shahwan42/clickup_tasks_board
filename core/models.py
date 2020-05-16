from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _


class Entity(models.Model):
    """ClickUp entity base model"""

    clickup_id = models.PositiveIntegerField(_("ClickUp ID"), unique=True)
    is_active = models.BooleanField(_("is active?"), null=True)
    name = models.TextField(_("name"), max_length=2048, null=True)
    description = models.TextField(_("description"), null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}, ClickUp_id: {self.clickup_id}>"


class Team(models.Model):
    """Starting point
    ClickUp Team representation"""

    clickup_id = models.PositiveIntegerField(_("ClickUp ID"), unique=True)
    name = models.CharField(_("name"), max_length=255)
    is_active = models.BooleanField(_("is active?"), default=True)

    def __str__(self):
        return self.name


class Space(Entity):
    """ClickUp Space representation"""

    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="spaces", null=True, blank=True
    )

    def __str__(self):
        return self.name


class Folder(Entity):
    """ClickUp Folder representation"""

    space = models.ForeignKey(
        Space, on_delete=models.CASCADE, related_name="folders", null=True, blank=True
    )

    def __str__(self):
        return self.name


class List(Entity):
    """ClickUp List representation"""

    folder = models.ForeignKey(
        Folder, on_delete=models.CASCADE, related_name="lists", null=True, blank=True
    )

    def __str__(self):
        return self.name

    # TODO in case of folderless lists, don't do it until asked strongly
    # force current structure for lower cost
    # space = models.ForeignKey(
    #     Space, on_delete=models.CASCADE, related_name="lists", null=True, blank=True
    # )


class Task(Entity):
    """ClickUp Task representation"""

    clickup_id = models.CharField(_("ClickUp ID"), max_length=12, unique=True)
    created_json = JSONField(_("TaskCreated JSON Response"), null=True, blank=True)
    updated_json = JSONField(_("TaskUpdated JSON Response"), null=True, blank=True)
    _list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )
    status = models.CharField(_("status"), max_length=100, null=True, blank=True)

    @property
    def list_clickup_id(self):
        if self._list:
            return self._list.clickup_id

    @property
    def list_name(self):
        if self._list:
            return self._list.name

    @property
    def user_name(self):
        if self.user:
            return self.user.name

    @property
    def user_email(self):
        if self.user:
            return self.user.email


class Webhook(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="webhooks", null=True, blank=True
    )
    clickup_id = models.CharField(_("ClickUp ID"), max_length=50, unique=True)
    created_json = JSONField(_("ClickUp JSON Response"), null=True, blank=True)

    def __str__(self):
        if self.created_json:
            return self.created_json.get("webhook").get("endpoint")

    def __repr__(self):
        return f"<Webhook, ClickUp_id: {self.clickup_id}>"
