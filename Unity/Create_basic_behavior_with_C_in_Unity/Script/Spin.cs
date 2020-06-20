using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[DisallowMultipleComponent]
[RequireComponent (typeof(KillBall))]
public class Spin : MonoBehaviour
{
    // Start is called before the first frame update
    [Tooltip ("Movimiento Hombre")]
    public float spinSpeed; 

    // Update is called once per frame
    void Update()
    {
        transform.Rotate (Vector3.up, spinSpeed*Time.deltaTime);
    }
}
