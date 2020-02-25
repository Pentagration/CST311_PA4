from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
def myNetwork():

    net = Mininet( topo=None, build=False, ipBase='10.0.0.0/8')
    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    r1 = net.addHost('r1', cls=Node, ip='10.0.1.1/8')
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    s1,s2 = [net.addSwitch(s) for s in 's1', 's2']
    net.addLink(s1,r1, intfName2='r1-eth1',params2={'ip':'10.0.1.1/8'})
    net.addLink(s2,r1, intfName2='r1-eth2',params2={'ip':'192.168.0.1/24'})
    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.100/8', defaultRoute='via 10.0.1.1')
    h2 = net.addHost('h2', cls=Host, ip='192.168.0.50/24', defaultRoute='via 192.168.0.1')
    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(s1,s2)

    info( '*** Starting network\n')
    net.build()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
~
