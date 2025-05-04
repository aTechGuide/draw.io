from diagrams import Diagram, Cluster
from diagrams.aws.general import MobileClient
from diagrams.aws.security import WAF
from diagrams.aws.network import APIGateway, ELB
from diagrams.aws.database import Elasticache, Dynamodb
from diagrams.aws.compute import ECS
from diagrams.aws.storage import S3


def generate_newlines(count):
    """
    Generate a string with the specified number of newline characters.

    Args:
        count (int): The number of newline characters to generate.

    Returns:
        str: A string containing `count` newline characters.
    """
    return "\n" * count


graph_attr = {
    "bgcolor": "black",
    "fontcolor": "white",
    "penwidth": "3",
    "fontname": "Gloria Hallelujah",
    "fontsize": "55",
    "ranksep": "2.0",
    "nodesep": "2.0",
    "pad": "1",
    # "margin": "5",
    # "labelloc": "b",
    # "size": "20,20"
}

cluster_attr = {
    "pad": "3",
    "labelloc": "c",
    "labeljust": "c",
    "fontname": "Gloria Hallelujah",
    "fontsize": "45",
    # "ranksep": "2.0",
    # "nodesep": "2.0",
    "margin": "30",
    "bgcolor": "#67AB9F",  # Light gray for clusters
    "fontcolor": "black", # Bright blue for cluster labels
    "pencolor": "#444444" # Darker border for clusters
    
}

edge_attr = {
    "penwidth": "12",  # Makes the arrows thicker
    "color": "#B85450" 
}

node_attr = {
    "fontname": "Gloria Hallelujah",
    "fontsize": "35",  # Set font size for all nodes
    "labelloc": "b",   # Place the label below the icon
    "labeldistance": "10",  # Increase the distance between the icon and the label
    "fontcolor": "black", #changed to black
    "ranksep": "2.0",
    "nodesep": "2.0",
    
}

with Diagram("WhatsApp Signup High Level Architecture", show=True, direction="LR", outformat="png", graph_attr=graph_attr, edge_attr=edge_attr, node_attr=node_attr):
    with Cluster("\n\tClient Side\t", graph_attr=cluster_attr):
        client = MobileClient("\n\n\n\n\nMobile App")
        
    with Cluster("\nAPI Layer", graph_attr=cluster_attr):
        n_api = generate_newlines(9)
        api = APIGateway(f"{n_api}API\nGateway")
        auth = ECS(f"{n_api}User\nService")
        cache = Elasticache(f"{n_api}OTP\nCache")
        
    with Cluster("\n\tData Layer\t", graph_attr=cluster_attr):
        n_api = generate_newlines(1)
        db = Dynamodb(f"{n_api}User\nDatabase")
        
    client >> api >> auth
    auth >> cache
    auth >> db
