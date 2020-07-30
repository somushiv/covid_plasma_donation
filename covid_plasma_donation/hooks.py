# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "covid_plasma_donation"
app_title = "Covid Plasma Donation"
app_publisher = "Hemolife Service Pvt Ltd"
app_description = "COVID19 plasma registry"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hemolifeservice@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/covid_plasma_donation/css/covid_plasma_donation.css"
# app_include_js = "/assets/covid_plasma_donation/js/covid_plasma_donation.js"

# include js, css files in header of web template
# web_include_css = "/assets/covid_plasma_donation/css/covid_plasma_donation.css"
# web_include_js = "/assets/covid_plasma_donation/js/covid_plasma_donation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "covid_plasma_donation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "covid_plasma_donation.install.before_install"
# after_install = "covid_plasma_donation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "covid_plasma_donation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"covid_plasma_donation.tasks.all"
# 	],
# 	"daily": [
# 		"covid_plasma_donation.tasks.daily"
# 	],
# 	"hourly": [
# 		"covid_plasma_donation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"covid_plasma_donation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"covid_plasma_donation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "covid_plasma_donation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "covid_plasma_donation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "covid_plasma_donation.task.get_dashboard_data"
# }

