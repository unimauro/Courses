using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[DisallowMultipleComponent]
public class DistanceBasedGradient1 : MonoBehaviour
{
    public Transform target;
    public Gradient  colorGradient;
    public float     maxDistance, intensity;

    private Material mat;

    void Awake()
    {
        mat = GetComponent<Renderer>().material;
    }
    void Update()
    {
        float ratio = Vector3.Distance(transform.position, target.position) / maxDistance;
        ratio = 1 - ratio;
        mat.color = colorGradient.Evaluate(ratio) * intensity;
    }
}
