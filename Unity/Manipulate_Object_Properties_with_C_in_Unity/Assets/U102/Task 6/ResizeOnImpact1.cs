using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[DisallowMultipleComponent]
[RequireComponent(typeof(Rigidbody))]
public class ResizeOnImpact1 : MonoBehaviour
{
    [Range (-0.99f, 0.99f)]
    public float ResizePercentage;
    [Range(0.01f,0.5f)] 
    public float destroyAtScale;

    private void OnCollisionEnter (Collision other)
    {
        transform.localScale *= 1 + ResizePercentage;

        if (transform.localScale.x < destroyAtScale)
            Destroy(gameObject);
    }
}