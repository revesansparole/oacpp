from os import environ as env

for key in sorted(env.keys()):
    print "env", key, env[key]
