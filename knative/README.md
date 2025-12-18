I had a kubernates version mismatch due to which my pods were crashing

the minimum version required was 1.32 but i had 1.31.5


`kubectl set env deployment/net-kourier-controller -n knative-serving KUBERNETES_MIN_VERSION=v1.31.5`

` kubectl set env deployment/activator -n knative-serving KUBERNETES_MIN_VERSION=v1.31.5`

`kubectl set env deployment/autoscaler -n knative-serving KUBERNETES_MIN_VERSION=v1.31.5`

`kubectl set env deployment/webhook -n knative-serving KUBERNETES_MIN_VERSION=v1.31.5`

`kubectl set env deployment/controller -n knative-serving KUBERNETES_MIN_VERSION=v1.31.5`


the setup commands are in the manifests directory and rest of the commands were ran using `kn`


```bash
➜  knative git:(main) ✗ kubectl get ksvc 
NAME    URL                                        LATESTCREATED   LATESTREADY   READY   REASON
hello   http://hello.default.172.18.0.2.sslip.io   hello-00002     hello-00002   True   
```