from django.shortcuts import render

# Create your views here.
def post_list(request):
	return render(request, 'blog/post_list.html', {})


'''
post_list함수는 request를 넘겨받아 render메소드를 호출한다.
render메소가 return한 blog/post_list.html템플릿을 보여준다.
'''