+++
title = 'Getting follow feature'
date = 2024-08-09T15:35:53+10:00
draft = false
+++ 

Since our server is entirely static, we are unable to directly process follow requests from ActivityPub platforms without some form of server-side processing. However, once a user sends a follow request to our static user, any content we publish can be shared with their [Inbox](https://www.w3.org/TR/activitypub/#inbox). 

There are three possible solutions to this problem:
1. [Setting manuallyApprovesFollowers to false in Actor object]({{< relref "#manually_approves_followers_tag" >}}) - Might not work with some platforms
2. [Adding requested follower to followers.json without sending Accept activity to origin server]({{< relref "#ignore_follow_request" >}})
3. [Periodically boots up a backend server and process the request]({{< relref "#backend_request" >}})

## Setting ManuallyApprovesFollowers Tag {#manually_approves_followers_tag} 

Some ActivityPub platforms, like Mastodon, can detect whether a user on another platform supports automatic acceptance of follow requests. This is determined by checking the `manuallyApprovesFollowers` field within the actor object of that user. To set this up, you can configure your actor object as follows:

```json
{
	"@context": "https://www.w3.org/ns/activitystreams",
	"type": "Person",
	"preferredUsername": "noah",
	"id": "https://noah.netlify.app/noah/actor.json",
	"inbox": "https://noah.netlify.app/noah/inbox.json",
	"outbox": "https://noah.netlify.app/noah/outbox.json",
	"followers": "https://noah.netlify.app/noah/followers.json",
	"following": "https://noah.netlify.app/noah/following.json",
	"publicKey": {
		"id": "https://noah.netlify.app/noah/actor.json#main-key", 
		"owner": "https://noah.netlify.app/noah/actor.json",
		"publicKeyPem": "..."
	},
	"manuallyApprovesFollowers": false
}
```
Setting `"manuallyApprovesFollowers": false` indicates to some ActivityPub platforms that the user of your instance automatically approves follow requests. This eliminates the need to send back an `Accept` activity.

## Adding Requested Follower Without Accept Activity {#ignore_follow_request}

When a user of an instance send out a follow request to our static hosted server. It enables us to share any already existing posts on our static site with that particular users by sending a [Create](https://www.w3.org/TR/activitypub/#create-activity-inbox) activity to his/her inbox. However, to access to his/her outbox, we need to have access to that user actor object to retrieve the inbox url. It's important that we have a way to store those information. See [Publishing Post](/page/extra/publish_post_feature) to understand how to share contents with other users.


## Running Backend To Process Follow Request {#backend_request}

To handle sending [Accept](https://www.w3.org/TR/activitypub/#accept-activity-inbox) activities back to followed users, we can set up a simple backend server on our local computer. This server would be available for a limited time each day. Additionally, we can provide a basic contact method on our static site, allowing followed users to notify us about follow requests so that we can address them appropriately.

### Example Program of Accept Activity

```python
import request 
from ActivityHandler import *

# URL pointing to your actor object
actor_id = "https://noah.netlify.app/noah/actor.json"

# Path to the private key generated using the "generate-keys.js" algorithm
private_key_path = "..."


# Activity Information 
# Retrieved from our local backend server 
follow_id = "..."

handler = ActivityHandler(actor_id, private_key_path)
handler.send_accept_activity(
	follow_id=follow_id
)

```
---
**References**
- [Adding ActivityPub to Your Static Site](https://paul.kinlan.me/adding-activity-pub-to-your-static-site/)
- [Follow Activity](https://www.w3.org/TR/activitypub/#follow-activity-inbox)
- [Accept Activity](https://www.w3.org/TR/activitypub/#accept-activity-inbox)


---
**See also**
- [Running ActivityPub Server on Static Site](/page/running_activitypub_server_leveraging_static_web_hosting/)
- [Publishing Post](/page/extra/publish_post_feature)
- [Codebase](/page/extra/activitypub_codebase)


