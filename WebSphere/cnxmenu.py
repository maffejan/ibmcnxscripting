import sys
class myMenu:
    items = []

    def AddItem( self, text, function ):
        self.items.append( {'text': text, 'func':function} )

    def Show( self ):
        c = 1
        print '\n\tWebSphere and Connections Administration'
        print '\t----------------------------------------', '\n'
        for l in self.items:
            # print c, l['text'], "\n"
            print '\t',
            print c, l['text']
            c = c + 1
        print

    def Do( self, n ):
        self.items[n]['func']()

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

def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )

if __name__ == "__main__":
    m = myMenu()
    m.AddItem( "Configure DataSources", cfgDataSource )
    m.AddItem( 'Backup J2EE Roles of all Applications', cfgJ2EERoleBackup )
    m.AddItem( 'Restore J2EE Roles of all Applications', cfgJ2EERoleRestore )
    m.AddItem( 'Set J2EE Roles initially (restricted)', cfgJ2EERolesRestricted )
    m.AddItem( 'Set J2EE Roles initially (unrestricted)', cfgJ2EERolesUnrestricted )
    m.AddItem( 'Configure JVM Heap Sizes', cfgJVMHeap )
    m.AddItem( 'Configure SystemOut/Err Log Size', cfgLogFiles )
    m.AddItem( 'Configure Monitoring Policy', cfgMonitoringPolicy )
    m.AddItem( 'Check if all Apps are running', checkAppStatus )
    m.AddItem( 'Check Database connections', checkDataSource )
    m.AddItem( 'Check JVM Heap Sizes', checkJVMHeap )
    m.AddItem( 'Check SystemOut/Err Log Sizes', checkLogFiles )
    m.AddItem( 'Check / Show all used ports', checkPorts )
    m.AddItem( 'Show WebSphere Variables', checkVariables )
    m.AddItem( 'Work with Files Policies', cnxFilesPolicies )
    m.AddItem( 'Work with Libraries', cnxLibraryPolicies )
    m.AddItem( 'Check External ID (all Apps & Profiles)', cnxMemberCheckExIDByEmail )
    m.AddItem( 'Deactivate and Activate a User in one step', cnxMemberDeactAndActByEmail )
    m.AddItem( 'Deactivate a User by email address', cnxMemberInactivateByEmail )
    m.AddItem( 'Synchronize ExtID for all Users in all Apps', cnxMemberSyncAllByEXID )
    m.AddItem( "Exit", bye )

state = 'True'
while state == 'True':
    m.Show()
    n = input( "your choice> " )
    m.Do( n - 1 )