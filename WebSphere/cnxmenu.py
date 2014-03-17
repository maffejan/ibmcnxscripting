# Author: Christop Stoettner
# E-Mail: info@stoeps.de
#

import sys
import os

# Load all jython commands, when they are not loaded
try:
    test = Scheduler.listAllTasks()
    if test == '':
        raise Exception
except:
    print 'Load Connections Commands'
    execfile("loadAll.py")

class cnxMenu:
    menuitems = []

    # Function to add menuitems
    def AddItem( self, text, function ):
        self.menuitems.append( {'text': text, 'func':function} )

    # Function for printing
    def Show( self ):
        c = 1
        print '\n\tWebSphere and Connections Administration'
        print '\t----------------------------------------', '\n'
        for l in self.menuitems:
            print '\t',
            print c, l['text']
            c = c + 1
        print

    def Do( self, n ):
        self.menuitems[n]["func"]()

def cfgDataSource():
    execfile( "cfgDataSource.py" )

def cfgJ2EERoleBackup():
    execfile( "cfgJ2EERoleBackup.py" )

def cfgJ2EERoleRestore():
    execfile( "cfgJ2EERoleRestore.py" )

def cfgJ2EERolesRestricted():
    execfile( "cfgJ2EERolesRestricted.py" )

def cfgJ2EERolesUnrestricted():
    execfile( "cfgJ2EERolesUnrestricted.py" )

def cfgJVMHeap():
    execfile( "cfgJVMHeap.py" )

def cfgLogFiles():
    execfile( "cfgLogFiles.py" )

def cfgMonitoringPolicy():
    execfile( 'cfgMonitoringPolicy.py' )

def checkAppStatus():
    execfile( 'checkAppStatus.py' )

def checkDataSource():
    execfile( 'checkDataSource.py' )

def checkJVMHeap():
    execfile( 'checkJVMHeap.py' )

def checkLogFiles():
    execfile( 'checkLogFiles.py' )

def checkPorts():
    execfile( 'checkPorts.py' )

def checkVariables():
    execfile( 'checkVariables.py' )

def cnxFilesPolicies():
    execfile( 'cnxFilesPolicies.py' )

def cnxLibraryPolicies():
    execfile( 'cnxLibraryPolicies.py' )

def cnxMemberCheckExIDByEmail():
    execfile( 'cnxMemberCheckExIDByEmail.py' )

def cnxMemberInactivateByEmail():
    execfile( 'cnxMemberInactivateByEmail.py' )

def cnxMemberDeactAndActByEmail():
    execfile( 'cnxMemberDeactAndActByEmail.py' )

def cnxMemberSyncAllByEXID():
    execfile( 'cnxMemberSyncAllByEXID.py' )

def cnxCommunitiesReparenting():
    execfile( 'cnxCommunitiesReparenting.py' )

def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )

if __name__ == "__main__":
    m = cnxMenu()
    m.AddItem( "Configure DataSources (cfgDataSource.py)", cfgDataSource )
    m.AddItem( 'Backup J2EE Roles of all Applications (cfgJ2EERoleBackup.py)', cfgJ2EERoleBackup )
    m.AddItem( 'Restore J2EE Roles of all Applications (cfgJ2EERoleRestore.py)', cfgJ2EERoleRestore )
    m.AddItem( 'Set J2EE Roles initially (restricted) (cfgJ2EERolesRestricted.py)', cfgJ2EERolesRestricted )
    m.AddItem( 'Set J2EE Roles initially (unrestricted) (cfgJ2EERolesUnrestricted.py)', cfgJ2EERolesUnrestricted )
    m.AddItem( 'Configure JVM Heap Sizes (cfgJVMHeap.py)', cfgJVMHeap )
    m.AddItem( 'Configure SystemOut/Err Log Size (cfgLogFiles.py)', cfgLogFiles )
    m.AddItem( 'Configure Monitoring Policy (cfgMonitoringPolicy.py)', cfgMonitoringPolicy )
    m.AddItem( 'Check if all Apps are running (checkAppStatus.py)', checkAppStatus )
    m.AddItem( 'Check Database connections (checkDataSource.py)', checkDataSource )
    m.AddItem( 'Check JVM Heap Sizes (checkJVMHeap.py)', checkJVMHeap )
    m.AddItem( 'Check SystemOut/Err Log Sizes (checkLogFiles.py)', checkLogFiles )
    m.AddItem( 'Check / Show all used ports (checkPorts.py)', checkPorts )
    m.AddItem( 'Show WebSphere Variables (checkVariables.py)', checkVariables )
    m.AddItem( 'Work with Files Policies (cnxFilesPolicies.py)', cnxFilesPolicies )
    m.AddItem( 'Work with Libraries (cnxLibraryPolicies.py)', cnxLibraryPolicies )
    m.AddItem( 'Check External ID (all Apps & Profiles) (cnxMemberCheckExIDByEmail.py)', cnxMemberCheckExIDByEmail )
    m.AddItem( 'Deactivate and Activate a User in one step (cnxMemberDeactAndActByEmail.py)', cnxMemberDeactAndActByEmail )
    m.AddItem( 'Deactivate a User by email address (cnxMemberInactivateByEmail.py)', cnxMemberInactivateByEmail )
    m.AddItem( 'Synchronize ExtID for all Users in all Apps (cnxMemberSyncAllByEXID.py)', cnxMemberSyncAllByEXID )
    m.AddItem( 'Reparent/Move Communities (cnxCommunitiesReparenting.py)', cnxCommunitiesReparenting )
    m.AddItem( "Exit", bye )

state = 'True'
while state == 'True':
    m.Show()
    n = input( "your choice> " )
    m.Do( n - 1 )
