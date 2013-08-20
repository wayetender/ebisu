=====
Ebisu
=====

.. image:: https://travis-ci.org/wayetender/ebisu.png?branch=master
    :target: https://travis-ci.org/wayetender/ebisu
    :alt: Travis CI Build Status

Ebisu health checker

--- Health Test Spec File ---

@example_test
Test: Initial Problem
	If 10 seconds has passed since this test last ran
	And "example.com" does not respond to pings 
	Then email "lucas@gmail.com" once
	And run command "ec2-reboot-instances i-3ea74257"

@example_test @tag2
Test: Big Problem
	If test "Initial Problem" has failed 3 times in the last 2 minutes
	And "example.com" does not respond to pings
	Then email "lucas@gmail.com" with subject "ALERT -- EXAMPLE.COM DOWN FOR GOOD -- GIVING UP"
	And disable actions on "Initial Problem" and "Big Problem"


--- Action / Condition Python Implementations ---


@action('email "{email}"')
@action('email "{email}" with subject "{subject}"')
def email(ctx, email, subj = None):
	subject = subj if subj else "%s is failing! EOM" % (ctx.test_name)
	emaillib.send_message(email, , "")


@conditon('"{server}" does not respond to pings')
def check_ping(ctx, server):
	return network_lib.can_ping(server)


--- RUNNING IT ---

import healthcheck

healthcheck.initialize({
	"DATABASE_URL": "sqlite:///",
	"TESTS_DIR": "healthtests/",
	"EMAILS": {
		"MASTER_EMAIL": "lucas@kavaanu.com",
		"NOTIFY_ON_STATUS_CHANGE": True
	}
})
while True:
	healthcheck.heartbeat()
	time.sleep(10)


--- Object Model ---


Test Status: GOOD, CHECKING, ALARM, DISABLED, EXCEPTION
Action Status: ACTIVE, DISABLED, EXCEPTION
Condition Status: FIRING, NOT_FIRING, EXCEPTION

Test: {test_name, tags, current_status, last_run, conditions, actions, run_history}
Test History Item: {test_name, event_time, status, logs}

Condition: {test_name, condition_name, current_status, run_history}
Condition History Item: {test_name, condition_name, event_time, logs}

Action: {test_name, action_name, current_status, run_history}
Action History Item: {test_name, action_name, event_time, logs}

Logs: [str]
Tags: [str]


--- User Interface ---


READ-ONLY -- the health spec should represent the current tests (entirely declarative)

Tests Page: view all tests, filter by tags
	table view: test name, current status, last run, click to reveal test detail
	button to run test now

Test Detail: view conditions/actions, color code by status
	click to reveal run history, 
	button to test action or condition