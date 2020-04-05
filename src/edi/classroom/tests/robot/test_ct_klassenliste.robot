# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.classroom -t test_klassenliste.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.classroom.testing.EDI_CLASSROOM_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/classroom/tests/robot/test_klassenliste.robot
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

Scenario: As a site administrator I can add a Klassenliste
  Given a logged-in site administrator
    and an add Klassenliste form
   When I type 'My Klassenliste' into the title field
    and I submit the form
   Then a Klassenliste with the title 'My Klassenliste' has been created

Scenario: As a site administrator I can view a Klassenliste
  Given a logged-in site administrator
    and a Klassenliste 'My Klassenliste'
   When I go to the Klassenliste view
   Then I can see the Klassenliste title 'My Klassenliste'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Klassenliste form
  Go To  ${PLONE_URL}/++add++Klassenliste

a Klassenliste 'My Klassenliste'
  Create content  type=Klassenliste  id=my-klassenliste  title=My Klassenliste

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Klassenliste view
  Go To  ${PLONE_URL}/my-klassenliste
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Klassenliste with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Klassenliste title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
