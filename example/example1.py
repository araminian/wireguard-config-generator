import wireguard_config_generator.models.models as wg_models
from wireguard_config_generator.generator import *      

Interface1 = wg_models.InterfaceModel(
    PrivateKey = wg_models.KeyModel(Key="yAnz5TF+lXXJte14tji3zlMNq+hd2rYUIgJBgB3fBmk="),
    ListenPort = 51820,
    CommentKey = "Interface" ,
    CommentValue = "WG0"
)

peer1 = wg_models.PeerModel(
    PublicKey = wg_models.KeyModel(Key="yAnz5TF+lXXJte14tji3zlMNq+hd2rYUIgJBgB3fBmk="),
    PreSharedKey = wg_models.KeyModel(Key="yAnz5TF+lXXJte14tji3zlMNq+hd2rYUIgJBgB3fBmk="),
    AllowedIPs = ["192.168.1.1/32","10.100.1.2/32"],
    Endpoint = wg_models.EndpointModel (
        Address = "10.100.10.40",
        Port = 123
    ),
    CommentKey = "User" , 
    CommentValue = "ARMIN"
)


peer2 = wg_models.PeerModel(
    PublicKey = wg_models.KeyModel(Key="yAnz5TF+lXXJte14tji3zlMNq+hd2rYUIgJBgB3fBmk="),
    PreSharedKey = wg_models.KeyModel(Key="yAnz5TF+lXXJte14tji3zlMNq+hd2rYUIgJBgB3fBmk="),
    AllowedIPs = ["192.168.1.2/32","10.100.1.2/32"],
    Endpoint = wg_models.EndpointModel (
        Address = "2607:5300:60:6b0::c05f:543",
        Port = 1234
    ),
    CommentKey = "User" , 
    CommentValue = "JACK"
)

peers = []
peers.append(generate_peer(peer1))
peers.append(generate_peer(peer2))

configComponents = wg_models.ConfigComponentsModel(
    Interface = generate_interface(Interface1),
    Peers = peers,
    ConfigPath = '/home/armin/wg/wg.conf'
)

generate_wg_conf_file(configComponents)
