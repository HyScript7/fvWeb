import routes.api.v1
import routes.web.root
import routes.web.wiki
import routes.web.forum
import routes.web.home
import routes.web.admin

routes = [(routes.web.root.web, ""), (routes.web.home.web, "/home/"),(routes.web.wiki.web, "/wiki/"), (routes.web.admin.web, "/admin/"), (routes.web.forum.web, "/forum/"), (routes.api.v1.api, "/api/v1/")]
