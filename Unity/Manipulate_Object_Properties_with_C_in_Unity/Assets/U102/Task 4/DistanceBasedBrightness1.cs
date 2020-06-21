using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[DisallowMultipleComponent]
public class DistanceBasedBrightness1 : MonoBehaviour
{
    public Transform target;
    public Color     baseColor;
    public float     maxDistance, intensity;

    private Material mat;

    void Awake()
    {
        mat = GetComponent<Renderer>().material;
    }
    void Update()
    {
        float ratio = Vector3.Distance(transform.position, target.position) / maxDistance;
        
        float brightness = 1 - ratio;
        mat.color = baseColor * brightness * intensity;
    }
}
