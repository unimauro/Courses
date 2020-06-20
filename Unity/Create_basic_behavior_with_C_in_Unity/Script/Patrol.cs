using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Patrol : MonoBehaviour
{
	public int distance;
	public float speed;
	private Vector3 startPos, endPos, targetPos;

	private void Awake()
	{
		startPos = transform.position;
		endPos = startPos
           + transform.forward
           * distance;
	}

	void Update()
	{
		if (Vector3.Distance(transform.position, startPos)<=0.1)
		{
			targetPos=endPos;
		}
		if (Vector3.Distance(transform.position,endPos)<=0.1)
		{
			targetPos=startPos;
		}
		transform.position = Vector3.MoveTowards (transform.position, targetPos, speed * Time.deltaTime);
	}



}
