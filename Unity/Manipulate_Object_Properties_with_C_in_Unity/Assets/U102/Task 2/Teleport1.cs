using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[DisallowMultipleComponent]
[RequireComponent(typeof(Collider))]
public class Teleport1 : MonoBehaviour
{
    public float teleportRange;
    
    void OnMouseDown()
    {
        transform.position += new Vector3 (
                Random.Range(-teleportRange, teleportRange),
                Random.Range(-teleportRange, teleportRange),
                Random.Range(-teleportRange, teleportRange)
        );    
    }
}