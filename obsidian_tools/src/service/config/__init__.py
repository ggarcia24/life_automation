from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="OBSITOOLS",
    settings_files=['settings.toml', '.secrets.toml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.
