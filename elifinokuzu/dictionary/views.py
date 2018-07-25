from django.shortcuts import render
from dictionary.models import Node
# Create your views here.

def index(request):

      nodes = Node.objects.all()

      return render(request, 'index.html', {
        'title': 'öküzün elifi',
        'nodes': nodes,
      })

def node_detail(request, id):
      Node = Node.objects.get(id=id)
      incoming = node.incoming.all()
      outcoming = node.outcoming.all()
      return render(request, 'node_detail.html', {
            'node': node,
            'incoming': incoming,
            'outcoming': outcoming,
            'title': 'Öküzün Elifi: %s' %node.name,
       })