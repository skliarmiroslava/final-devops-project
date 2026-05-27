
resource "kubernetes_namespace" "argocd" { 
  metadata {
    name = "argocd"                        
  }
}

#Install ArgoCD into EKS using Helm chart

resource "helm_release" "argocd" {
  name       = "argocd"

  repository = "https://argoproj.github.io/argo-helm"

  chart      = "argo-cd"

  namespace  = kubernetes_namespace.argocd.metadata[0].name

  create_namespace = false

  version = "7.7.11"

  # Load custom Helm values for ingress and DNS configuration

  values = [
    file("${path.module}/argocd-values.yml")
  ]
}
