+++
title = 'Getting follow feature'
date = 2024-08-09T15:35:53+10:00
draft = false
+++ 

Since our server is entirely static, it is not possible for us to receive follow requests from an ActivityPub platform without some form of server-side processing.

What sort of information do I need to send out here?
1. How it's not important for us to send back an 'Accept' request, if a user has sent us a followed requests. We can still share contents back to the followed users
2. Alternatively, we can run a backend server once in a while to check for any 
follow requests. Then make appropriate actions and update our static site accordingly.
2.1. Additionally, we can include some form of contact information on our 


---
**See also**
- [Running ActivityPub Server on Static Site](/page/running_activitypub_server_leveraging_static_web_hosting/)
- [Codebase](/page/extra/activitypub_codebase)