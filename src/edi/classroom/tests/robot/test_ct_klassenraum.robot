# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.classroom -t test_klassenraum.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.classroom.testing.EDI_CLASSROOM_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/classroom/tests/robot/test_klassenraum.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Klassenraum
  Given a logged-in site administrator
    and an add Klassenraum form
   When I type 'My Klassenraum' into the title field
    and I submit the form
   Then a Klassenraum with the title 'My Klassenraum' has been created

Scenario: As a site administrator I can view a Klassenraum
  Given a logged-in site administrator
    and a Klassenraum 'My Klassenraum'
   When I go to the Klassenraum view
   Then I can see the Klassenraum title 'My Klassenraum'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Klassenraum form
  Go To  ${PLONE_URL}/++add++Klassenraum

a Klassenraum 'My Klassenraum'
  Create content  type=Klassenraum  id=my-klassenraum  title=My Klassenraum

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Klassenraum view
  Go To  ${PLONE_URL}/my-klassenraum
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Klassenraum with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Klassenraum title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
