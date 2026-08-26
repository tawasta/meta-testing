##############################################################################
#
#    Author: Futural Oy
#    Copyright 2021- Futural Oy (https://futural.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    "name": "Futural Base",
    "summary": "Setup basic Odoo instance configuration",
    "version": "19.0.1.1.2",
    "category": "Administration",
    "website": "https://github.com/tawasta/futural",
    "author": "Futural",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "auto_install": True,
    "depends": [
        # Add technical features
        "base_technical_features",
        # Allows regular users to access the text-based domain selector in search
        "base_filter_domain_selector_without_debug_mode",
        # Adds partner number for partners
        "base_partner_sequence",
        # Auto-update modules
        "module_auto_update",
        # Auto-update modules on a schedule
        "module_auto_update_schedule",
        # Sets auth case insensitive
        "auth_user_case_insensitive",  ## OCA
        # Verify email on signup
        # "auth_signup_verify_email", ## OCA
        # Adds user roles and role history
        # "base_user_role_history", ## OCA
        # Forces secure passwords
        # "password_security", ## OCA
        # Remove odoo.com Bindings
        "disable_odoo_online",
        # Remove Odoo branding from sent mails
        "mail_debrand",  ## OCA
        # Hide enterprise-only apps and features
        "remove_odoo_enterprise",
        # Export installation information to SWKB
        "software_knowledge_base_exporter",
        # Lets the user expand a dialog box to the full screen width
        "web_dialog_size",
        # Environment ribbon. The message will be auto-deleted
        "web_environment_ribbon",
        # Hides help bubbles which are used to introduce odoo
        "web_no_bubble",  ## OCA
        # Provides a responsive/mobile compliant backend interface
        "web_responsive",
        # Adds a button next to refresh the displayed list.
        "web_refresher",
        # Adds company-specific colors
        # "web_company_color", ## OCA
        # Disable autoinvite when creating a new user
        "auth_signup_disable_autoinvite",
        # Invite mail and custom system name eg. Futural
        "auth_signup_invite_mail_system_name",
        # Ability to invite users with mass action
        "auth_signup_mass_action_invite",
        # Auditlog security group to read auditlogs
        "auditlog_security_group",
        # Auditlogs for partner records
        "partner_auditlog_rules",
        # Group expand
        # "web_group_expand", ## OCA
        # Ability to search ir_ui_view by external id and module
        "ir_ui_view_search",
        "scheduler_error_mailer_futural_template",
    ],
    "data": [
        "data/ir_config_parameter.xml",
        "data/ir_default.xml",
        "data/res_partner.xml",
        "data/res_users.xml",
    ],
}  # type: ignore
